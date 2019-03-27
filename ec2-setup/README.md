# Setup You EC2

### Setup Development Tools
```
sudo yum update -y
sudo yum groupinstall "Development Tools"
```
Now, you will have python 2.7.

### Install Node.js 8:
```
curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
sudo yum -y install nodejs
```

### Enable the EPEL repository

  * Please see this [FAQ - EC2 enable EPEL](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-enable-epel/)
    - `vim /etc/yum.repos.d/epel.repo`
    - Locate and change the entry enabled=0 to enabled=1 that is located in the $basearch section of the epel.repo file.
    - `sudo yum-config-manager --enable epel`
    - `sudo yum --enablerepo=epel install zabbix`

### Add Repositories for Amazon Linux
  - default launch with two Repositories: `amzn-main` and `amzn-updates`.
  - List the installed yum repositories with the following command:

    `yum repolist all`

  - enable a yum repository in `/etc/yum.repos.d`

    `sudo yum-config-manager --enable <repo id>`

    such as `epel` for `<repo id>`.

  - reference this [link](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/add-repositories.html)

### Setup `cmake`
```
wget https://cmake.org/files/v3.8/cmake-3.8.0.tar.gz
tar -zxf cmake-3.8.0.tar.gz
cd cmake-3.8.0
./configure
make
sudo make install
```

### Install OpenSSL
  * Note: Please visit [Openssl website](https://www.openssl.org/source/) to get latest OpenSSL

```
wget https://www.openssl.org/source/openssl-1.1.0f.tar.gz
tar -xvzf openssl-1.0.2k.tar.gz
cd openssl-1.0.2k
./config --prefix=/usr/
make
sudo make install
```
  * Check openssl version

```
openssl version -a
```

### Hardlink/Softlink Protection
  * For security, recommend to do this. See the [blog](http://danwalsh.livejournal.com/64493.html)
  * Add two lines to `/etc/sysctl.d/00-defaults.conf`

```
# Hardlink/Softlink Protection
fs.protected_hardlinks = 1
fs.protected_symlinks = 1
```

  * validate the change
    * `sudo sysctl -a | grep fs`
    * check the results with
    ```
    fs.protected_hardlinks = 1
    fs.protected_symlinks = 1    
    ```

### Save an AMI for you
  * After your AMI saved, run `sudo reboot` because let hardlink/softlink protection take effects.
