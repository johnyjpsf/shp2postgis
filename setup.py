import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shp2postgis",
    version="0.1.1",
    author="Johny Patrick da Silva Ferreira",
    author_email="johnypatrick5@gmail.com",
    description="shapefile to sql converter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnyjpsf/shp2posgis",
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
