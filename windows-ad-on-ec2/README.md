# Build your active directory in AWS EC2

## Part1: Launch EC2
* Images: `Microsoft Windows Server 2016 Base`
* t2.2xlarge
* Add customize scripts

	```
	<powershell>
	Rename-Computer -NewName "DC01" -Restart
	</powershell>
	```
![](./images/1-dc.png)


## Part2: Winodws AD Secruity Group
![](./images/2-dc.png)
![](./images/3-dc.png)

## Part3: Config the AD

1. Logon the EC2 windows server. Verify the computer name.

	![](./images/4-dc.png)

2. run PowerShell command:

	```
	Add-WindowsFeature AD-Domain-Services -IncludeManagementTools
	```

	![](./images/5-dc.png)

3. Command line to open Server Manager. In the right up corner, promote this server as domain controller.

	![](./images/6-dc.png)
	
4. Deploy a new forest
	
	![](./images/7-dc.png)

	* NetBIOS name: `BEYOUNG`

5. After completing the wizard, the server will be restarted and the server will be ready to be used. 

## Part4: Add a domain user

1. Command line to open Server Manager. In the right up corner `Tools`, choose Active Directory Users and Computers.
	
	![](./images/8-dc.png)
	![](./images/9-dc.png)

2. Add a user
	
	![](./images/11-dc.png)

3. Add DC user to the `Domain Admins` Group

	![](./images/19-dc.png)

* **Notes: You must create a new user here. Later on, you can't use local administrator to login your EC2.**

## Part5: Add a server into the DC

1. Launch an windows EC2 instance. In the Advanced Details add user data script: 

	```
	<powershell>
	Rename-Computer -NewName "SRV01" -Restart
	</powershell>
	```
	
	![](./images/10-dc.png)

2. Logon to the windows EC2. Open file manager, right click properties on 'This PC`.

	![](./images/12-dc.png)

	* Control Panel > System and Security > System

	![](./images/13-dc.png)

3. Get the following error messages:

	![](./images/14-dc.png)

4. Change the network DNS record to the DC01 private ip.

	![](./images/15-dc.png)
	![](./images/16-dc.png)

5. Join the domain again.

	![](./images/17-dc.png)
	![](./images/18-dc.png)
	
6. Restart your computer to take the effection.

## Part6: Use the domain name to login

1. In the DC, make sure the login format of the domain user, which can use email format as login.

	![](./images/19-dc.png)
	![](./images/20-dc.png)

2. In the remote desktop configuration, change to the domain user login:

	![](./images/21-dc.png)
	![](./images/22-dc.png)

3. Now, you can login to your SRV01 using the DC users.

	![](./images/23-dc.png)
	![](./images/24-dc.png)
