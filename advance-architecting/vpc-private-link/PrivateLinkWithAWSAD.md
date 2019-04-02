# PrivateLink and Secrets manager

## Setup DHCP Options

* Create DHCP Options Sets
  ![](./images/6-dns.png)
  ![](./images/7-dns.png)

We use the secrets manager as the example to verify the private link setting.

* Service endpoint: `secretsmanager.us-east-1.amazonaws.com`
* check the `ipconfig/all`
  ![](./images/0-dns.png)

* the result of `nslookup secretsmanager.us-east-1.amazonaws.com`
  ![](./images/1-dns.png)


## Setup the private links

Go to the service `VPC`
  ![](./images/2-dns.png)
  
* Create the endpoint
  ![](./images/3-dns.png)
  ![](./images/4-dns.png)
  ![](./images/5-dns.png)

* Now, the secrets manager becomes the local ip. The AWS AD server can know the ip.
  ![](./images/8-dns.png)


