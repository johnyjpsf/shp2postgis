import shapefile

class ShapeFileReader:
    def __init__(self, shapeFileName, srid=4326, encoding="latin1"):
        self.layerName = shapeFileName
        self.encoding = encoding
        self.srid = str(srid)
        self.layer = None

    def getFields(self):
        fieldTypes = {}
        try:
            for field in self.layer.fields:
                if field[0] != "DeletionFlag":
                    fieldTypes[field[0]] = field[1]
            return fieldTypes
        except Exception as e:
            return False

    def getFeatures(self):
        return self.layer.shapeRecords()

    def getData(self):
        data = []
        for fea in self.layer.shapeRecords():
            feaDict = fea.record.as_dict().copy()
            wkt = fea.shape.shapeTypeName + str(fea.shape.points).replace("[","(").replace("]",")").replace(", "," ")
            feaDict["WktShapeFileGeometry"] = wkt
            feaDict["WktShapeFileGeometrySrid"] = self.srid
            data.append(feaDict)
        return data

    def load(self):
        try:
            self.layer = shapefile.Reader(self.layerName, encoding=self.encoding)
            return self
        except Exception as e:
            print("Camada " + self.layerName + " não pode ser lida.")
            return False
