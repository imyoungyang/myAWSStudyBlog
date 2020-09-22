# AWS Geospatial

* PostGIS extenstion on PostgreSQL on Amazon RDS [link](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts.General.FeatureSupport.Extensions.101x)
    * Aurora Serverless version 10.7
        * PostGIS: 2.4.4
    * RDS for PostgreSQL v12.3
        * PostGIS: 3.0.0

## Use Aurora Serverless

#### Installation

```
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
CREATE EXTENSION address_standardizer;
CREATE EXTENSION address_standardizer_data_us;
CREATE EXTENSION fuzzystrmatch;
CREATE EXTENSION postgis_tiger_geocoder;
select postgis_full_version();
```

And you can see the results:
```
POSTGIS="2.4.4" PGSQL="100" GEOS="3.6.2-CAPI-1.10.2 4d2925d6" PROJ="Rel. 4.9.3, 15 August 2016" GDAL="GDAL 2.1.4, released 2017/06/23" LIBXML="2.9.3" LIBJSON="0.12.99" LIBPROTOBUF="1.3.0" (core procs from "2.4.4" need upgrade) RASTER (raster procs from "2.4.4" need upgrade)
```

## Jupyter Notebook connect to Redshift

* Jaydebeapi [link](https://dwgeek.com/connect-postgresql-using-python-and-jdbc-driver-example.html/)
* psycopg2 and sqlalchemy [link](https://stackoverflow.com/questions/38937162/how-to-connect-jupyter-ipython-notebook-to-amazon-redshift) [doc](https://www.psycopg.org/docs/)

## Key Github of labs

* Spatial Data Science with PySAL [2020](https://github.com/knaaptime/pysal-scipy20), [2019](https://github.com/pysal/scipy2019-intermediate-gds), [2018](https://github.com/geopandas/scipy2018-geospatial-data)
* Movingpandas [link](https://github.com/anitagraser/movingpandas)
* postGIS tutorials [link](https://learn.crunchydata.com/postgis/)
* postGIS workshop [link](https://postgis.net/workshops/postgis-intro/)

## Glue connections
* security group: self-referencing inbound rule for ALL Traffic. [link](https://docs.aws.amazon.com/glue/latest/dg/setup-vpc-for-glue-access.html)
* s3 vpcend point for vpc-subnet: Could not find S3 endpoint or NAT gateway for subnetId

## ML - trajectory geospatial temporal
* [movingpandas](https://github.com/anitagraser/movingpandas)
* [scikit-mobility](https://github.com/scikit-mobility/scikit-mobility)

## Geospatial Opensources
* [Open source for geospatial](https://github.com/inspire-helsinki-2019/challenge/issues/14)
* geomesa [link](https://www.geomesa.org/)
* [EU INSPIRE GEOPORTAL](https://inspire-geoportal.ec.europa.eu/)
* [PostGIS - SQLAlchemy, GeoAlchemy, GeoPandas](https://atmamani.github.io/cheatsheets/open-geo/postgis-2/) and [link](https://gis.stackexchange.com/questions/239198/adding-geopandas-dataframe-to-postgis-table)