import shapefile

## Módulo instalado
from shp2postgis.Util import *

## Local no projeto
# from Util import *

class Data2Sql:
    """
    # schema:    string | database's schema
    # tableName: string | schema's table
    # encoding:  string | charset to read file
    # file:      string | shapefile's path
    """
    def __init__(self, file, tableName, schema="public", encoding="latin1"):
        self.schema = schema
        self.tableName = tableName
        self.encoding = encoding
        self.file = file
        self.stripFields = ["WktShapeFileGeometry", "WktShapeFileGeometrySrid", "gid"]
        self.replacedChars = {
                '\x00':'',
                "'":"''",
                "":"''"
            }
        try:
            with shapefile.Reader(self.file, encoding=self.encoding) as shp:
                fieldTypes = {}
                for field in shp.fields:
                    if field[0] != "DeletionFlag":
                        fieldTypes[field[0]] = field[1]
                        self.fields = fieldTypes
        except Exception as e:
            print('problema para carregar arquivo')
            self.fields = None

    def getFields(self):
        return self.fields

    def translateShape(self, shape):
        text = "ST_SetSRID(ST_GeomFromGeoJSON('"
        if shape.shapeTypeName == 'NULL':
            text = 'NULL'
        else:
            geojson = str(shape.__geo_interface__)
            text = text + geojson.replace('(','[').replace(')',']').replace("'",'"') + "')," + self.getSrid() + ")"
        return text

    def getSrid(self):
        return '4326'

    def getGeomType(self):
        return 'GEOMETRY'

    def getDropTable(self):
        return "DROP TABLE IF EXISTS \"{sch}\".\"{tab}\";\n".format(sch=self.schema, tab=self.tableName)

    """
    "C": Characters, text.
    "N": Numbers, with or without decimals.
    "F": Floats (same as "N").
    "L": Logical, for boolean True/False values.
    "D": Dates.
    "M": Memo, has no meaning within a GIS and is part of the xbase spec instead.
    """
    def getCreateTable(self, columnsToLower=False):
        typeDict = {
            "C": "VARCHAR",
            "N": "NUMERIC",
            "F": "FLOAT",
            "L": "BOOLEAN",
            "D": "DATE",
            "M": "VARCHAR"
        }
        sqlString = "CREATE TABLE \"{sch}\".\"{tab}\" (\"gid\" SERIAL, CONSTRAINT \"{tab}_pk\" PRIMARY KEY (\"gid\"));\n".format(sch=self.schema, tab=self.tableName)
        sqlString += "SELECT AddGeometryColumn(\'{sch}\',\'{tab}\',\'geom\',{srid},\'{typ}\',2);\n".format(sch=self.schema, tab=self.tableName, srid=self.getSrid(), typ=self.getGeomType())
        for field in self.getFields():
            field_ = field
            if columnsToLower:
                field_ = field.lower()

            if field not in self.stripFields:
                sqlString += "ALTER TABLE \"{sch}\".\"{tab}\" ADD COLUMN \"{col}\" {typ};\n".format(sch=self.schema, tab=self.tableName, col=field_, typ=typeDict[self.getFields()[field]])
        return sqlString

    def makeInsert(self, record, geom, columnsToLower=False):
        attributes = []
        if "gid" in record:
            del record["gid"]
        for attr in record:
            text = ""
            if record[attr] == None:
                text = "NULL"
            else:
                if self.getFields().setdefault(attr, "M") == 'C' or self.getFields().setdefault(attr, "M") == 'D':
                    if type(record[attr]) == bytes:
                        text = record[attr].decode()
                        if text == '':
                            text = 'NULL'
                    else:
                        text = str(record[attr])
                        for key in self.replacedChars:
                            if key in text:
                                text = text.replace(key, self.replacedChars[key])
                        text = "'" + text + "'"
                        if text == "''":
                            text = "NULL"
                elif self.getFields().setdefault(attr, "M") == 'M':
                    break
                else:
                    text = str(record[attr])
            attributes.append(text)
        values = ", ".join(attributes)
        quotedFields = []
        for value in self.getFields().keys():
            if value not in self.stripFields:
                if columnsToLower:
                    value = value.lower()
                quotedFields.append('"' + value + '"')
        fieldsString = ", ".join(quotedFields)
        return "INSERT INTO \"{schema}\".\"{tableName}\" ({fldStr}, \"geom\") VALUES ({val}, {geo});\n".format(schema=self.schema, tableName=self.tableName, fldStr=fieldsString, val=values, geo=geom)

    def writeSqlFile(self, fileName, columnsToLower=False):
        listWriter(self.getDropTable(), self.getCreateTable(columnsToLower), fileName=fileName, fileExtension="sql",separator=None, mode='wt')
        with shapefile.Reader(self.file, encoding=self.encoding) as shp:
            for feature in shp.iterShapeRecords():
                record = feature.record.as_dict().copy()
                geom = self.translateShape(feature.shape)
                insert = self.makeInsert(record, geom, columnsToLower)
                listWriter(insert, fileName=fileName, fileExtension="sql",separator=None, mode='at')
