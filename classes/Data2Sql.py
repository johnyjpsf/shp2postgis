class Data2Sql:
    """
    # schema: string | database's schema
    # table:  string | schema's table
    # data:   list   | list of records as dictionaries
    # fields: list   | list of fields as dictionaries, key: name of attribute, value: type of data
    """
    def __init__(self, table, fields, data, schema="public"):
        self.schema=schema
        self.table=table
        self.data = data
        self.fields = fields
        self.stripFields = ["WktShapeFileGeometry", "WktShapeFileGeometrySrid", "gid"]

    def getDropTable(self):
        sqlString = "DROP TABLE \"{sch}\".\"{tab}\";\n".format(sch=self.schema, tab=self.table)
        return sqlString

    """
    "C": Characters, text.
    "N": Numbers, with or without decimals.
    "F": Floats (same as "N").
    "L": Logical, for boolean True/False values.
    "D": Dates.
    "M": Memo, has no meaning within a GIS and is part of the xbase spec instead.
    """
    def getCreateTable(self):
        dict = {
            "C": "VARCHAR",
            "N": "NUMERIC",
            "F": "FLOAT",
            "L": "BOOLEAN",
            "D": "DATE",
            "M": "VARCHAR"
        }
        sqlString = "CREATE TABLE \"{sch}\".\"{tab}\" (\"gid\" SERIAL, CONSTRAINT \"{tab}_pk\" PRIMARY KEY (\"gid\"));\n".format(sch=self.schema, tab=self.table)
        for field in self.fields:
            if field not in self.stripFields:
                sqlString += "ALTER TABLE \"{sch}\".\"{tab}\" ADD COLUMN \"{col}\" {typ};\n".format(sch=self.schema, tab=self.table, col=field, typ=dict[self.fields[field]])
        return sqlString

    def getInserts(self):
        inserts = []
        for fea in self.data:
            attributes = []
            WktShapeFileGeometry = ""
            WktShapeFileGeometrySrid = ""
            if "gid" in fea:
                del fea["gid"]
            if "WktShapeFileGeometry" in fea:
                WktShapeFileGeometry = fea["WktShapeFileGeometry"]
                del fea["WktShapeFileGeometry"]
            if "WktShapeFileGeometrySrid" in fea:
                WktShapeFileGeometrySrid = fea["WktShapeFileGeometrySrid"]
                del fea["WktShapeFileGeometrySrid"]
            for attr in fea:
                text = ""
                if fea[attr] == None:
                    text = "NULL"
                else:
                    if self.fields.setdefault(attr, "M") == 'C' or self.fields.setdefault(attr, "M") == 'D':
                        text = str(fea[attr]).replace('\x00','').replace("'","\\" + "'")
                        text = "'" + text + "'"
                        if text == "''":
                            text = "NULL"
                    elif self.fields.setdefault(attr, "M") == 'M':
                        break
                    else:
                        text = str(fea[attr])
                attributes.append(text)
            values = ", ".join(attributes)
            geometry = "ST_GeomFromText('" + WktShapeFileGeometry + "', " + WktShapeFileGeometrySrid + ")"
            quotedFields = []
            for value in self.fields.keys():
                if value not in self.stripFields:
                    quotedFields.append('"' + value + '"')
            fieldsString = ", ".join(quotedFields)
            insert = "INSERT INTO \"{schema}\".\"{table}\" ({fldStr}, \"geom\") VALUES ({val}, {geom});\n".format(schema=self.schema, table=self.table, fldStr=fieldsString, val=values, geom=geometry)
            inserts.append(insert)
        return inserts
