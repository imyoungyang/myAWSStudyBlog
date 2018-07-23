# DMS

* Oracle performance tuning: [link](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Configuration)

* LogMiner or Binary Reader
	* Binary Reader has less chance of having I/O or CPU impact.
	* For migrations with a high volume of changes, CDC performance is usually much better when using Binary Reader compared with using Oracle LogMiner.
	* Binary Reader supports the following HCC compression types: query high, archive high, archive low
	* HCC more information on [link](http://www.oracle.com/technetwork/testcontent/o10compression-082302.html)

* Custom CDC time: Specify a time from which to begin processing changes. DMS will need access to source database changes beginning at this time (via binary logs, redo logs, wal logs, etc.)

* Determine the total latency, or replica lag, for a task by combining the **CDCLatencySource** and **CDCLatencyTarget** values. reference the [link](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html)

* [Setup Oracle Endpoint](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
* [MSSQL](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html)
	* Must config full backup 

### How Much Load Will the Migration Process Add to My Source Database?

This a complex question with no specific answer. The load on a source database is dependent upon several things. 
	
During a migration, AWS DMS performs a full table scan of the source table for each table processed in parallel. Additionally, each task periodically queries the source for change information. To perform change processing, you may be required to increase the amount of data written to your databases change log. If your tasks contain a Change Data Capture (CDC) component, the size, location, and retention of log files can have an impact on the load. [link](https://d0.awsstatic.com/whitepapers/RDS/AWS_Database_Migration_Service_Best_Practices.pdf)

# Amazon Kinesis Stream
* [Streaming Changes in a Database with Amazon Kinesis](https://aws.amazon.com/blogs/database/streaming-changes-in-a-database-with-amazon-kinesis/)

# Data Fetch Frequece
### DMS
* [Connection Attributes](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html)
	* MySQL: Default value: 5 (mins) can change to 1 (min) for idle
	* PostgreSQL: dependeces on captuerDDLs
	* Oracle: Supplemental Log / Logminer Reader
		* Use Oracle Streams Performance Advisor (SPADV) statistics script to get the performance. Usually latency is less 1 mins. [link page 31](http://www.oracle.com/technetwork/database/availability/maa-gg-performance-1969630.pdf)

### Glue
* Glue is batch oriented.
* Schedule jobs at minimum of 5 mins

# References
* [Monitoring the Oracle Streams Topology and Performance](https://docs.oracle.com/cd/B28359_01/server.111/b28321/strms_topology.htm#STRMS170)
* [Oracle GoldenGate Performance Best Practices](http://www.oracle.com/technetwork/database/availability/maa-gg-performance-1969630.pdf) Appendex C script for Streams Performance Advisor (SPADV, page 31)
* [Database Migration—What Do You Need to Know Before You Start?](https://aws.amazon.com/blogs/database/database-migration-what-do-you-need-to-know-before-you-start/)
* [DMS best practices](https://d0.awsstatic.com/whitepapers/RDS/AWS_Database_Migration_Service_Best_Practices.pdf)
* [Glue FAQ](https://aws.amazon.com/glue/faqs/)