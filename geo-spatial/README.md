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
