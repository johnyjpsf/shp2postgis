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

### Para usar como biblioteca / as a library

```python
from shp2postgis.Shp2Postgis import Shp2Postgis

process = Shps2Postgis(dictInput, outputPath, schema, encoding, srid, verbose)

process.run()
```

#### Parâmetros / parameters
* >dictInput:
>>dicionário python em que cada item tem chave sendo o nome da camada e valor sendo o caminho para o arquivo shapefile
>
>> python dictionary in which each item has a key being the layer name and value being the path to the shapefile
>
>```json
dictInput = {
    "airport": "/home/user/SHP/AIRPORT",
}
```

* >outputPath:
>>diretório onde será gravado o arquivo sql.
>
>>folder where the sql file will be saved.
>
>```python
outputPath = "/home/user/SQL/"
```

* >schema:
>>schema do banco de dados em que o sql será carregado.
>
>>database schema where sql file will be loaded.
>
>```python
schema = "public"
```

* >encoding:
>>conjunto de caracteres do shapefile.
>
>>charset of the shapefile.
>
>```python
encoding = "latin1"
```

* >srid:
>>conjunto de caracteres do shapefile.
>
>>charset of the shapefile.
>
>```python
encoding = "latin1"
```

* >verbose:
>>deixe com valor False.
>
>>leave False.
>
>```python
verbose = False
```
