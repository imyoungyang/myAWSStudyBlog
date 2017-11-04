# AWS VPC Deep Dive Lab

## Objectives

At the end of this assignment you will have created a Shared services VPC using the following Amazon Web Services: EC2, VPC, VPC Peering, VPN Connections, Customer Gateway, and Virtual Private Gateway.

![](images/architecture1.png)

1. Learn how to connect two VPC in different AWS regions.
2. Restricted machine can't direct access. Only from left region VPC can ssh to restricted machine.
3. Restricted machine needs to update packages such as `yum install` command.
4. All other VPC connects to internet must pass the proxy to do the security control.


## Lab stages

- [Stage 1: the VPC, subnet, routing table and Internet Gateway](stage1-vpc.md)
- [Stage 2: Setup Customer Gateways Secruity Group](stage2-sg.md)
- [Stage 3: Setup Customer Gateway](stage3-cgw.md)
- [Stage 4: Setup Virtual Private Gateway and VPN Connections](stage4-vgw.md)
- [Stage 5: Connect VPN connections](stage5-vpn-tunnel.md)
- [Stage 6: Setup Proxy](stage6-proxy.md)
- [Stage 7: Auto scaling group](stage7-autoscaling.md)
- [Stage 8: Load Balancer for Squid Server](stage8-nlb.md)
- [Stage 9: network load balancer + Auto Scaling](stage9-nlb-asg.md)
- [Stage 10: VPC Peering](stage10-vpc-peering.md)


## Reference Links

- [Squid HA design in AWS](https://aws.amazon.com/articles/using-squid-proxy-instances-for-web-service-access-in-amazon-vpc-another-example-with-aws-codedeploy-and-amazon-cloudwatch/)
- [Enable proxy protocol on ELB](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-proxy-protocol.html)
- [Squid receive proxy protocol](ftp://ftp.arnes.si/packages/squid/squid-3.5.3-RELEASENOTES.html#toc2.7)
- [DX Gateway](https://aws.amazon.com/tw/blogs/aws/new-aws-direct-connect-gateway-inter-region-vpc-access/)