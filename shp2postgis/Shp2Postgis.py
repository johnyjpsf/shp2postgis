## Módulo instalado
from shp2postgis.Data2Sql import Data2Sql
from shp2postgis.Util import *
import os

## Local no projeto
# from Data2Sql import Data2Sql
# from Util import *

class Shp2Postgis:
    """
    # dictInput: dictionary as {"layerName": "path/shapeFileName", ....}
    """
    def __init__(self, dictInput, outputPath=".", schema="public", encoding="latin1", verbose=False, log=False, columnsToLower=False):
        self.dictInput = dictInput
        if outputPath == None:
            self.outputPath = "."
        else:
            if not outputPath.endswith(os.sep):
                outputPath = outputPath + os.sep
            self.outputPath = outputPath
        if schema == None:
            self.schema = "public"
        else:
            self.schema = schema
        if encoding == None:
            self.encoding = "latin1"
        else:
            self.encoding = encoding
        if verbose == None:
            self.verbose = False
        else:
            self.verbose = verbose
        if log == None:
            self.log = False
        else:
            self.log = log
        if columnsToLower == None:
            self.columnsToLower = False
        else:
            self.columnsToLower = columnsToLower

    def run(self):
        if type(self.dictInput) != dict:
            print('dicionário de input inválido')
            exit(1)
        for layerName in self.dictInput:
            shapeFileName = self.dictInput[layerName]
            if self.verbose:
                print("convertendo arquivo {file} para {layer}.sql".format(file=shapeFileName, layer=layerName))
            try:
                f = open(shapeFileName + ".shp","r")
                f.close()
            except Exception as e:
                print(shapeFileName + ".shp não existe")
                if self.verbose:
                    print(e)
                continue
            shapeReader = Data2Sql(tableName=layerName, schema=self.schema, encoding=self.encoding, file=shapeFileName + ".shp")
            shapeReader.writeSqlFile(fileName=self.outputPath + layerName, columnsToLower=self.columnsToLower)
        if self.verbose:
            print("processo terminado!")
