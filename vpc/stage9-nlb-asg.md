# Stage 9: network load balancer + Auto Scaling

In the end of this stage, you will integrate network load balancer and auto scaling group on proxy servers.

## Create auto scaling group

1. Create AMI images for squid. AMI Name: `squid-us-west-1`

	![](images/lab9/0-ami-image.png)
	
2. Create Launch Configuration
	- select MyAMI: `squid-us-west-1`
	
	![](images/lab9/1-asg-create.png)
	
3. select ec2 instance: t2.micro
4. Launch configuration
	- Name: asg-proxy
	- Auto give public ip
	
	![](images/lab9/2-asg-create.png)
	
5. Checked delete on termintion for EBS storage.
6. Security group: select exisiting `sg-proxy`

	![](images/lab9/3-asg-create.png)

7. Review and create launch group.

## Create Auto Scaling Group

1. config auto scaling group
	- Name: asg-proxy
	- Group size: start 0
	- Network: vpc-172.20.0.0/16
	
	![](images/lab9/4-asg-create.png)
	
2. In the advance details
	- target group: nlb-proxy
	- Healthy type: ELB

	![](images/lab9/5-asg-create.png)

3. define the scale out policy

	![](images/lab9/6-asg-create.png)

4. Use default notifcation and Notification
5. Name tag: asg-proxy
6. Done: create the asg-proxy

	![](images/lab9/7-asg-create.png)
	
## Verify Auto Scaling Group with NLB

7. Change the asg-proxy, desire 2.

	![](images/lab9/8-asg-create.png)

8. In the instances, you will see two instances are creating.

	![](images/lab9/10-asg-create.png)
	
9. In the target group: nlb-proxy, you will see **three** instances are in the group.

	![](images/lab9/9-asg-create.png)	

10. You can edit and remove `proxy-13.57.3.42` machine. You will see the status become **draining**.

	![](images/lab9/11-asg-create.png)
	
11. Testing the NLB and autoscaling group at the restricted machine. Run `yum update` at the restricted machine:

	![](images/lab9/12-asg-testing.png)
	
12. In the nlb monitoring tab, you can see the cloud watch with traffic records.

	![](images/lab9/13-asg-cloud-watch.png)
	
# Take away

Now, you have the following architecture diagram:

![](images/lab9/0-architecture.png)

Congradulations! You learn a lot of key things for AWS VPC.