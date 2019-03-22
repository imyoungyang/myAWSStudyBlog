
# VPC Privatelinks and Route53 Resolver

In this lab, you will implement the following architecture diagram:

![](./images/architecture.png)

## VPC Setup
* Region: `us-west-2`
* IP: `172.18.0.0/16`
* public sub: `172.18.0.0/24` and turn on the auto-assign public ip

![](./images/0-dc.png)

## Build your active directory in AWS EC2
* Images: `Microsoft Windows Server 2016 Base`
* t2.2xlarge
* Add customize scripts
![](./images/1-dc.png)

```
<powershell>
Rename-Computer -NewName "DC01" -Restart
</powershell>
```

## Winodws AD Secruity Group
![](./images/2-dc.png)
![](./images/3-dc.png)

## Config the AD
![](./images/4-dc.png)

PowerShell

```
Add-WindowsFeature AD-Domain-Services -IncludeManagementTools
```

![](./images/5-dc.png)

* Command line to open Server Manager. In the right up corner. Promote this server as domain controller.

![](./images/6-dc.png)
![](./images/7-dc.png)

* NetBIOS name: `BEYOUNG`
* After completing the wizard, the server will be restarted and the server will be ready to be used. 

![](./images/8-dc.png)
![](./images/9-dc.png)

## Add a domain user

![](./images/11-dc.png)

* Add DC user to the `Domain Admins` Group

![](./images/19-dc.png)

* **Notes: You must create a new user here. Later on, you can't use local administrator to login your EC2.**

## Add a server into the DC

![](./images/10-dc.png)


```
<powershell>
Rename-Computer -NewName "SRV01" -Restart
</powershell>
```

* Add to domain

![](./images/12-dc.png)

* Control Panel > System and Security > System

![](./images/13-dc.png)
![](./images/14-dc.png)

* Change the network DNS record to the DC01 private ip.

![](./images/15-dc.png)
![](./images/16-dc.png)

* Join the domain again.

![](./images/17-dc.png)
![](./images/18-dc.png)

* Restart your computer

## Use the domain name to login

In the DC, make sure the login format of the domain user.

![](./images/19-dc.png)
![](./images/20-dc.png)

In the remote desktop configuration, change to the domain user login:

![](./images/21-dc.png)
![](./images/22-dc.png)

Now, you can login to your SRV01 using the DC users.

![](./images/23-dc.png)
![](./images/24-dc.png)


## Deep Dive on the DNS setting

You will found that Windows AD can resolve the private link. The major reason is at the DNS Forwarder.

![](./images/27-dc.png)
![](./images/25-dc.png)
![](./images/26-dc.png)


If you remove the forwarder `.2` server, you found that you can not get the private link information:

![](./images/28-dc.png)

## Route 53 resolver

### Setup Rout53 Resolver

![](./images/32-dc.png)

### create the outbounds roles

![](./images/29-dc.png)

Now, you can get information for private AD information

![](./images/30-dc.png)

Also, when you query about the private links, you can get the correct results

![](./images/31-dc.png)

### Change CORP DNS forwarder to Route53 resolver inbound

![](./images/34-dc.png)

![](./images/33-dc.png)

Now, the corp machine can query AWS private links and private domain of AD such as `beyoung.com`

![](./images/35-dc.png)