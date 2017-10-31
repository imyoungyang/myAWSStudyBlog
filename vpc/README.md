# AWS VPC Deep Dive Lab

## Objectives

At the end of this assignment you will have created a Shared services VPC using the following Amazon Web Services: EC2, VPC, VPC Peering, VPN Connections, Customer Gateway, and Virtual Private Gateway.

![](images/architecture1.png)

1. Learn how to connect two VPC in different AWS regions.
2. Restricted machine can't direct access. Only from left region VPC can ssh to restricted machine.
3. Restricted machine needs to update packages such as `yum install` command.
4. All other VPC connects to internet must pass the proxy to do the security control.


## Lab stages

1. [Stage 1: Building the VPC, subnet, routing table and Internet Gateway](stage1.md)
2. [Stage 2: Setup Customer Gateways Secruity Group](stage2.md)
3. [Stage 3: Setup Customer Gateway](stage3.md)
4. [Stage 4: Setup Virtual Private Gateway and VPN Connections](stage4.md)
5. [Stage 5: Connect VPN connections](stage5.md)
