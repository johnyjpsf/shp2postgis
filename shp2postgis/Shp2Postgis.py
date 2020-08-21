from shp2postgis.Data2Sql import Data2Sql
from shp2postgis.ShapeFileReader import ShapeFileReader
from shp2postgis.Util import *

class Shp2Postgis:
    """
    # dictInput: dictionary as {"layerName": "path/shapeFileName", ....}
    """
    def __init__(self, dictInput, outputPath="./", schema="public", encoding="latin1", srid=4326, verbose=False):
        self.dictInput = dictInput
        if outputPath == None:
            self.outputPath = "./"
        else:
            self.outputPath = outputPath
        if schema == None:
            self.schema = "public"
        else:
            self.schema = schema
        if encoding == None:
            self.encoding = "latin1"
        else:
            self.encoding = encoding
        if srid == None:
            self.srid = 4326
        else:
            self.srid = srid
        if verbose == None:
            self.verbose = verbose
        else:
            self.verbose = verbose

    def run(self):
        for layerName in self.dictInput:
            shapeFileName = self.dictInput[layerName]
            if self.verbose:
                print("convertendo arquivo {file} para {layer}.sql".format(file=shapeFileName, layer=layerName))
            try:
                f = open(shapeFileName + ".shp","r")
                f.close()
            except Exception as e:
                if self.verbose:
                    print(shapeFileName + ".shp não existe")
                continue
            layer = ShapeFileReader(shapeFileName, encoding=self.encoding, srid=self.srid)
            if not layer.load():
                continue
            converter = Data2Sql(schema=self.schema, table=layerName, fields=layer.getFields(), data=layer.getData())
            listWriter(converter.getDropTable(), converter.getCreateTable(), converter.getInserts(), fileName=self.outputPath + layerName, fileExtension="sql",separator=None)
        if self.verbose:
            print("processo terminado!")
