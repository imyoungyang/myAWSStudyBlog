#/bin/bash

ip=$(curl http://169.254.169.254/latest/meta-data/public-ipv4)
echo "Code Server"
echo "http://$ip:8443"
security_group=$(ec2-metadata -s | cut -d " " -f 2);
aws ec2 authorize-security-group-ingress --group-name $security_group --protocol tcp --port 8443 --cidr 0.0.0.0/0
version="2.1698"
vsc_version="1.41.1"
wget https://github.com/cdr/code-server/releases/download/$version/code-server$version-vsc$vsc_version-linux-x86_64.tar.gz
# wget https://github.com/codercom/code-server/releases/download/$version/code-server-$version-linux-x64.tar.gz
tar -xvzf code-server$version-vsc$vsc_version-linux-x86_64.tar.gz
cd code-server$version-vsc$vsc_version-linux-x86_64
chmod +x code-server
./code-server --port 8443
