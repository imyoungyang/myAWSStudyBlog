# Streaming Concepts

Ask What / Where / When / How questions:

  - What results are being calculated?
  - Where in event time?
  - When in processing time?
  - How do refinements of results relate?

* recommend reading through the [Streaming 101] (https://www.oreilly.com/ideas/the-world-beyond-batch-streaming-101) [Streaming 102](https://www.oreilly.com/ideas/the-world-beyond-batch-streaming-102) post on O’Reilly Radar. And [The Evolution of Massive-Scale Data Processing](https://docs.google.com/presentation/d/10vs2PnjynYMtDpwFsqmSePtMnfJirCkXcHZ1SkwDg-s/present?slide=id.g63ca2a7cd_0_527)

## Key Design questions and mindset
  - micro-service with fast data
  - Streaming

## Comparison

* Kafa vs Queue
  - Kafa good things: consumers read the whole things.
  - Queue: consumers read and delete the message.
  - Kafa benefits: reduce the complexity from N*M links to N+M links

* Time Latency: Picosecond, nanoseconds, microseconds
  - < 10 ms
    - Streaming tools: Flink, Akka Streams, Kafka Streams
  - < 100 ms
    - Fast JVM message handlers: Akka Actors, LMAX Disruptor
    - "Micro-batch"
    - Incremental, micro-batch training of faster ML models. SQL query, group by, accumulate.
  - < 1 second
    - "Mini-batch"
    - Incremental ML model training for compute-intensive models

* High Volume
  - < 10K qps
    - REST
    - Process individually
  - < 100K qps
    - Nonblocking REST: eg parallel Akka actors
    - Process individually (? it depends)
  - < 1M qps
    - Flink or Spark Streaming
    - Process in bulk

* Which kinds of data processing, analytics?
  - Machine learning: training models, mini-bath to batch, dynamically training?
  - serve model: game score, leaderboard
  - Process individually: i.e. **Complex event processing (CEP)** usually lower volumes (<10k qps) with per-event overhead low such as cpu-on-fire.
  - Process bulk: usually datum's identity unimportant

* Apache Flink
  * High volume
  * Low latency
  * Beam Runner
  * Evolving SQL, ML

* Spark Streaming
  * Mini-batch model
  * > 0.5 second latency
  * Ideal for Rich SQL, ML


* Impala query engine to offer SQL-for-Hadoop

* [Beam Capability Matrix](https://beam.apache.org/documentation/runners/capability-matrix/)

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

* Fast data Architecture for streaming applications - Dean Wampler[video](https://www.youtube.com/watch?v=oCW5y4_8uGU), [slide](https://deanwampler.github.io/polyglotprogramming/papers/StreamAllTheThings.pdf)

* [re:Invent 2016: AWS Big Data & Machine Learning Sessions](https://aws.amazon.com/blogs/big-data/reinvent-2016-aws-big-data-machine-learning-sessions/#more-740)

* [Apache Flink: What How Why Who Where by Slim Baltagi](https://www.slideshare.net/sbaltagi/apacheflinkwhathowwhywhowherebyslimbaltagi-57825047)

* [Comparing Pig Latin and SQL for Constructing Data Processing Pipelines](http://yahoohadoop.tumblr.com/post/98294444546/comparing-pig-latin-and-sql-for-constructing-data)

* Pig
  - a platform for analyzing large data sets
  - Pig Latin is the relational data-flow language

* Tez
  - Tez is a framework for creating a complex directed acyclic graph (DAG) of tasks for processing data. (DAG- spark also use)
  - Pig and Hive can use Tez as running engine to gain better performance.
