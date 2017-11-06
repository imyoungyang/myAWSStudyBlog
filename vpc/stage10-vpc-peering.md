# Stage 10: VPC Peering

You will learn use `vpc peering` to connect 2 VPCs in the same region.

## Create a VPC

1. create a VPC in the `us-west-1`

	- Name: `vpc-172.18.0.0/16`
	- CIDR: `172.18.0.0/16`

2. Create a VPC Peering
	
	![](images/lab10/0-create-peering.png)
	
	- name: peer-172.18.0.0/16
	- requester: 172.18.0.0/16
	- accepter: 172.20.0.0/16
	
	![](images/lab10/1-create-peering.png)
	
3. Accept the peering request

	![](images/lab10/2-create-peering.png)
	
4. Edit route table `rtb-172.20.0.0/16`
	- add 172.120.0.0/16 to pcx peering
	
	![](images/lab10/3-create-peering.png)
	
5. Edit route table `rtb-172.18.0.0/16`
	- add 172.20.0.0/16 to pcx peering
	
	![](images/lab10/4-create-peering.png)
	
6. Edit security group `sg-172.18.0.0/16`

	![](images/lab10/5-sg.png)
	
## Verify VPC Peering

1. Create a subnet 172.18.0.0/24 at vpc-172.18.0.0/16

	![](images/lab10/6-subnet.png)

2. Launch an EC2 instance at sub-172.18.0.0/24
	- name: restricted-172.18.0.0
	- use existing security group `sg-172.18.0.0/16`

3. ssh to your strongwan machine and ping your ec2 machine at sub-172.18.0.0/24

	![](images/lab10/7-verify.png)
	
4. ssh to restricted machine at sub-172.120.0.0/24. Edit `/etc/yum.conf` and add the following line to the proxy

	```
	proxy=http://nlb-proxy-1ced42e7fcf40e9a.elb.us-west-1.amazonaws.com:3128
	```
	if FQDN did not work, change to the ip address of one of proxy server such as
	
	```
	proxy=http://172.20.1.64:3128
	```

5. execut yum update

	![](images/lab10/8-yum-update.png)

	**important** remember to add acl configuration in the `/etc/squid/suqid.conf` to allow 172.120.0.0/16.
	
## Take away

Now, you have the following diagram to connect two vpcs in the same region.

![](images/lab10/0-architecture.png)