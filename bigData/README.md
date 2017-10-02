* Impala query engine to offer SQL-for-Hadoop


* [Apache Flink on AWS](https://aws.amazon.com/blogs/big-data/build-a-real-time-stream-processing-pipeline-with-apache-flink-on-aws/)

* [Flink Stream processing refarch](https://github.com/awslabs/flink-stream-processing-refarch)

* [Flink Webnar](https://www.youtube.com/watch?v=MzTZp47Jy7E)

* [Elastic search with Flink](https://www.elastic.co/blog/building-real-time-dashboard-applications-with-apache-flink-elasticsearch-and-kibana)

* [Real-time in-memory OLTP and Analytics with Apache Ignite on AWS](https://aws.amazon.com/blogs/big-data/real-time-in-memory-oltp-and-analytics-with-apache-ignite-on-aws/)

* [Apache Ignite 中文 Manual](https://www.zybuluo.com/liyuj/note/230739)

* Kudu vs Parquet vs HBase
  - Kudu is column storage engine (like HBase). But it increased its scan speed.
    - Kudu’s data model is more traditionally relational, while HBase is schemaless.
    - Kudu’s on-disk representation is truly columnar and follows an entirely different storage design than HBase/BigTable.
  - Storage
    - Kudu store its data in Ext4 or XFS. Kudu is not in-memory database.
    - Parquet save on HDFS
  - Data formats
    - Closely resembles Parquet, with a few differences to support efficient random access as well as updates.

* [Waht is DataLake vs Data warehouse? Martin Fowler](https://martinfowler.com/bliki/DataLake.html)
  - datalake:
    - schemaless
    - keep raw data.
    - data lake as singular point for integrating data across an enterprise.
    - analytic purposes, not for collaboration between operational systems
  - data warehouse
    - consistent schema
    - data cleanse but also aggregate the data into a form that made it easier to analyze.

* [2017 01 performance comparison different file formats and storage engines](https://db-blog.web.cern.ch/blog/zbigniew-baranowski/2017-01-performance-comparison-different-file-formats-and-storage-engines)
  - Kudu
  - Parquet
  - HBase
  - Avro
  - mapfile

* [Analytic Database on AWS: Best Practices](https://www.cloudera.com/documentation/director/cloud/topics/cloud_analytic_db_best_practices.html)

* Data Engineering Workload
  - Transient Batch (most flexible)
  - Persistent Batch (most control)
  - Persistent Batch on HDFS (fastest)

![Data Engineering Workload](https://www.cloudera.com/documentation/director/cloud/images/xcloud_de-etl_all_patterns.png.pagespeed.ic.tZ2h1kn3c5.webp)

* HMS: Hive Metastore

![Persistent Batch on HDFS](https://www.cloudera.com/documentation/director/cloud/images/xcloud_de-etl_pattern03.png.pagespeed.ic.qcBYKlpuBi.webp)

* Transient Clusters vs Persistent Cluster
  - Transient clusters:
    - Recommended for lowest cost if clusters will be busy less than 50% of the time.
    - Most batch ETL and data engineering workloads are transient: they are intended to prepare a set of data for some downstream use, and the clusters don't need to stay up 24x7. A transient cluster is launched to run a particular job and is terminated when the job is done.
    - choose different cluster configurations for different jobs instead of running all jobs on the same permanent cluster with a particular configuration of hardware
