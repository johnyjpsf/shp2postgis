import unittest
from classes.Util import *

class verificaUtil(unittest.TestCase):

    # def test_template(self):
    #     #Arrange
    #     txt = "exemplo de teste"
    #     esperado = "exemplo_de_teste"
    #     #Act
    #     resultado = txt.replace(" ","_")
    #     #Assert
    #     self.assertEqual(esperado, resultado)

    def test_retorna_dicionario_quando_le_arquivo(self):
        #Arrange
        fileName = "/home/johny/dev/carregador-geoportal/app/tests/input/test_input_readDictFile.txt"
        esperado = {
        "airport":"aerodromo",
        "airspace":"espaco_aereo",
        "waypoint":"waypoint"
        }
        #Act
        dicionario = readDictFile(fileName)
        #Assert
        self.assertEqual(esperado, dicionario)

    def test_retorna_lista_quando_le_arquivo(self):
        #Arrange
        fileName = "/home/johny/dev/carregador-geoportal/app/tests/input/test_input_readListFile.txt"
        commentChar = "#"
        esperado = ["airspace","waypoint"]
        #Act
        resultado = readListFile(fileName, commentChar)
        #Assert
        self.assertEqual(esperado, resultado)
