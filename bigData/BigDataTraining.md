# Trend Big Data training

* Big Data Key Terms
  - Sources
    - internal
    - external
  - Formats
    - Structured
    - Unstructured
  - Speed
    - Real-time
    - Near Real-time
    - Batch
  - Analytics
    - Descriptive: (base on history, BI)
    - Prescriptive: (Predict: deep learning/ML)

### 計算存儲分離 (Storage vs Compute)
  - 兩邊對於 V (速度) & V (量) 需求不同
  - IoT: 數據和應用更加抽離
  - S3 version: can compare 這次和上次的結果比較，不同的 source version 比較。
  - Data oriented design

### Streaming Data
  - 信用卡反欺詐: 好幾千條 rule. in ms response fraud or not
  - Stock stream: sliding window
  - Athena like Presto, query on S3. 目的是不要搬資料..

### Data lake
  - Problem: Isolated Data silo, format, management, ETL.
  - Schema on Read. (不需要改變數據存處，根據Read需要改 Schema)
  - HDFS: 存數據，機器存取的錢是貴的。 並且需要 3 倍的資料 redundant.
  - Herd: Finra OpenSource project for management data on S3.

### Check Finra, Herd project.
  - [Herd](https://github.com/FINRAOS/herd)

### Lambda Architecture to Analyze Customer Behavior
  - [How SmartNews Built a Lambda Architecture on AWS to Analyze Customer Behavior and Recommend Content](https://aws.amazon.com/blogs/big-data/how-smartnews-built-a-lambda-architecture-on-aws-to-analyze-customer-behavior-and-recommend-content/)

   ![](https://dmhnzl5mp9mj6.cloudfront.net/bigdata_awsblog/images/SmartNewsImage1a.png)  

### AWS Data Lake Solutions

  - [AWS Data lake solutions cloud formation templates](http://docs.aws.amazon.com/solutions/latest/data-lake-solution/architecture.html)

   ![](http://docs.aws.amazon.com/solutions/latest/data-lake-solution/images/data-lake-solution-architecture.png)

### Athena
  - Save cost: 如果資料很大的時候，避免 Scan..所以需要先把資料轉成 column first. (Data Scanned - $5 / TB)
  - 應用場景為 Ad Hoc.
  - `MSCK` repair table, alter table.

### Redshift
  - DistKey and SortKey

  - [Choose the best sort key](http://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key.html)
    - If recent data is queried most frequently, specify the **timestamp** column as the leading column for the sort key.
    - If you do frequent range filtering or equality filtering on one column, specify that **column as the sort key**.
    - If you frequently **join a table**, specify the join column as both the **sort key and the distribution key**.

  - Distribution Styles: There are 3 types
    - [Distribution Styles](http://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html)
      - Even distribution: distributes the rows across the slices in a round-robin fashion

      - Key distribution: distributed according to the values in one column. The leader node will attempt to place matching values on the same node slice. Benefits for the **physically stored together**.

      - ALL distribution: A copy of the entire table is distributed to every node. Be appropriate only for relatively **slow moving tables** and **not updated frequently or extensively**.

    - Distribution Key best Practices
      - Balance data movement and workloads
      - *data movement*: Collocate the rows from joining tables: When the rows for joining columns are on the same slices, less data needs to be moved during query execution.
      - *workloads*: Distribute data evenly among the slices in a cluster: If data is distributed evenly, workload can be allocated evenly to all the slices.


      * DistKey 只有一個
      * SortKey 可以 combo

      ```
      CREATE TABLE system_errors3 (
        err_code INTEGER,
        created_at timestamp
      ) DISTKEY(created_at) SORTKEY(created_at);
      ```

### Redshift Spectrum
  - Automatic parallelization query on S3 (透過 parquet + Hive data schema)
  - Leader node 分析資料的來源是在 S3 or Redshift 上。Fact data at S3, hot data at Redshift.
    - create external table, location S3

### Redshift Spectrum vs Athena
  - [AWS Blog](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/)
    - Athena:
      - interactive ad-hoc queries
      - severless architecture
      - All the major BI tools and SQL clients that use JDBC can be used with Amazon Athena
      - Athena uses Presto and ANSI SQL, HiveQL for DDL statements.
    - Redshift Spectrum
      - on large sets of structured data
      - automatically scales out to thousands of instances. So queries run quickly, whether they are processing a terabyte, a petabyte, or even an exabyte.
      - Redshift is based on PostgreSQL 8.0.2.

### PostgreSQL vs MySQL
  - [SQL Statements different](https://wiki.postgresql.org/wiki/Things_to_find_out_about_when_moving_from_MySQL_to_PostgreSQL)
    - Database, table, field and columns names in PostgreSQL are case-independent, unless you created them with double-quotes around their name, in which case they are case-sensitive. In MySQL, table names can be case-sensitive or not, depending on which operating system you are using.
    - PostgreSQL and MySQL seem to differ most in handling of dates, and the names of functions that handle dates.
    - MySQL:  'foo' || 'bar' means 'foo' OR 'bar', 'foo' && 'bar' means 'foo' and 'bar'. But PostgreSQL, 'foo' || 'bar' = 'foobar'.

  - [Airflow](https://airflow.incubator.apache.org/): open source workflow engine.
