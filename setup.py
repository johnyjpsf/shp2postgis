import setuptools
from shp2postgis.Util import *

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shp2postgis",
    version=getVersion(),
    author="Johny Patrick da Silva Ferreira",
    author_email="johnypatrick5@gmail.com",
    description="shapefile to sql converter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnyjpsf/shp2postgis",
    packages=setuptools.find_packages(),
    keywords='gis geospatial geographic shapefile shapefiles postgis postgre sql database',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.6'
)

# apagar build antigo
# rm -r build && rm -r dist && rm -r shp2postgis.egg-info/

# empacotar
# python3 setup.py sdist bdist_wheel

# fazer upload
# python3 -m twine upload -u johnyjpsf -p meu_password --repository testpypi dist/*

# desinstalar o pacote antigo
# pip3 uninstall shp2postgis -y

# instalar o pacote
# pip3 install --index-url https://test.pypi.org/simple/ shp2postgis
