# shp2posgis

> Módulo python para converter arquivos no padrão shapefile da esri para arquivos sql que podem ser importados em bancos de dados postgresql/postgis.

> Python module to convert esri shapefile format to sql files that can be imported into postgresql/postgis database.

## Uso / Usage
> primeiro é necessário instalar as dependências

> First install dependencies

```bash
pip3 install -r requirements.txt
```
### python3 na linha de comando / on command line
> Uso detalhado pode ser visto usando:

> Details about use are shown using:

```bash
python3 shp2postgis.py -h
```
ou / or
```bash
python3 shp2postgis.py --help
```

> Para usar como biblioteca

> To use as library

```python
from Shps2Postgis import Shps2Postgis

process = Shps2Postgis(dictInput, outputPath, schema, encoding, srid, verbose)

process.run()
```
