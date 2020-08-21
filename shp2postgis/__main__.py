import sys, getopt
from shp2postgis import Util
from shp2postgis import Shp2Postgis

def main():
    help_ptbr =  "Uso: shp2sql [OPÇÃO]... --ifile=ARQUIVO \n"
    help_ptbr += " ou: shp2sql [OPÇÃO]... -i ARQUIVO \n"
    help_ptbr += "Converte os ARQUIVO(s) shapefile em SQL do PostgreSql com Postgis."
    help_ptbr += " Como o shapefile é um conjunto de arquivos não é necessário usar a extensão após o nome.\n"
    help_ptbr += "  -h, --help              Exibe este texto de ajuda.\n"
    help_ptbr += "  -i, --ifil=ARQUIVO      Arquivo de entrada com a lista de camadas e shapefiles.\n"
    help_ptbr += "                          Cada linha deve estar no formato <camada>=<path/shapeName>.\n"
    help_ptbr += "                          Uma linha pode ser comentada usando o caracter '#'.\n"
    help_ptbr += "  -o, --odir=DIRETÓRIO    Caminho para o diretório onde serão criados os arquivos .sql.\n"
    help_ptbr += "                          padrão: './'\n"
    help_ptbr += "  -s, --schema=ESQUEMA    Nome do esquema do banco de dados que será usado para criar as tabelas\n"
    help_ptbr += "                          padrão: 'public'\n"
    help_ptbr += "  -c, --srid=CODIGO       Código numérico para sistema de referência das geometrias. \n"
    help_ptbr += "                          padrão: '4326'\n"
    help_ptbr += "  -e, --encoding=CHARSET  Código para conjunto de caracteres que será usado na leitura do shapefile. \n"
    help_ptbr += "                          padrão: 'latin1'\n"
    help_ptbr += "Exemplos:\n"
    help_ptbr += "  python3 shp2sql.py -i ./shapes.txt \n"
    help_ptbr += "  python3 shp2sql.py --ifile=./shapes.txt --schema=\"ais\" --odir=./saida/"

    help_en =  "Usage: shp2sql [OPTION]... --ifile=FILE \n"
    help_en += "   or: shp2sql [OPTION]... -i FILE \n"
    help_en += "Converts shapefile FILE(s) in SQL PostgreSql/Postgis."
    help_en += " Shapefile is a set of files, so do not use extension after file name.\n"
    help_en += "  -h, --help              Show this help text.\n"
    help_en += "  -i, --ifil=FILE         Input file as a list of layers and shapefiles.\n"
    help_en += "                          Each line must be formated as <layer>=<path/shapeName>.\n"
    help_en += "                          Lines can be commented using '#' in the begin os the line.\n"
    help_en += "  -o, --odir=FOLDER       Path to output created SQL files.\n"
    help_en += "                          default: './'\n"
    help_en += "  -s, --schema=SCHEMA     Database schema name to be used on create table.\n"
    help_en += "                          default: 'public'\n"
    help_en += "  -c, --srid=CODE         Geometry reference system code. \n"
    help_en += "                          default: '4326'\n"
    help_en += "  -e, --encoding=CHARSET  Charset to be used on shapefile reader. \n"
    help_en += "                          default: 'latin1'\n"
    help_en += "Examples:\n"
    help_en += "  python3 shp2sql.py -i ./shapes.txt \n"
    help_en += "  python3 shp2sql.py --ifile=./shapes.txt --schema=\"ais\" --odir=./output/"

    inputFile = None
    outputDir = None
    schema = None
    srid = None
    encoding = None
    verbose = None

    try:
      opts, args = getopt.getopt(sys.argv[1:],"hHvi:o:s:c:e:",["help","help_en","ifile=","odir=","schema=","srid=","encoding=","verbose"])
    except getopt.GetoptError:
      print("Veja o uso da ferramenta executando 'python3 shp2sql.py -h'")
      sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help_ptbr)
            sys.exit(2)
        elif opt in ("-H", "--help_en"):
            print(help_en)
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--odir"):
            outputDir = arg
        elif opt in ("-s", "--schema"):
            schema = arg
        elif opt in ("-c", "--srid"):
            srid = arg
        elif opt in ("-e", "--encoding"):
            encoding = arg
        elif opt in ("-v", "--verbose"):
            verbose = True
        else:
            print("Parâmetro não esperado. Veja o uso da ferramenta executando 'python3 shp2sql.py -h'")
            sys.exit(2)

    if inputFile == None:
        print("Parâmetro --ifile obrigatório. Veja o uso da ferramenta executando 'python3 shp2sql.py -h'")
        sys.exit(2)

    lista = Util.readDictFile(fileName=inputFile, commentChar="#", separationChar="=")
    batchProcess = Shp2Postgis(dictInput=lista, outputPath=outputDir, schema=schema, encoding=encoding, srid=srid, verbose=verbose)
    batchProcess.run()

    sys.exit(0)

if __name__ == "__main__":
    main()
