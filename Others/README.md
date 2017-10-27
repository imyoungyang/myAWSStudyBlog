* [Natural Language Processing at Clemson University – 1.1 Million vCPUs & EC2 Spot Instances](https://aws.amazon.com/blogs/aws/natural-language-processing-at-clemson-university-1-1-million-vcpus-ec2-spot-instances/)

### 雷區
* Elastic Search Bulk Upload 100MB or 10MB limitation
[discuss forum](https://forums.aws.amazon.com/thread.jspa?threadID=217922)
  - error message: `{"Message":"Request size exceeded 10485760 bytes"}`

* Kibana Map Analysis default 是關起來的，必須自己手動打開 [Configuring Kibana to Use a WMS Map Server](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-kibana.html#es-managedomains-logstash)

* [Using a Proxy to Access Amazon ES from Kibana](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-kibana.html#es-managedomains-logstash)
