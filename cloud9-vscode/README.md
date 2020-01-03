ip=$(curl http://169.254.169.254/latest/meta-data/public-ipv4)
echo "Code Server"
echo "http://$ip:8443"
security_group=$(ec2-metadata -s | cut -d " " -f 2);
aws ec2 authorize-security-group-ingress --group-name $security_group --protocol tcp --port 8443 --cidr 0.0.0.0/0
version="1.32.0-310"
wget https://github.com/codercom/code-server/releases/download/$version/code-server-$version-linux-x64.tar.gz
tar -xvzf code-server-$version-linux-x64.tar.gz
cd code-server-$version-linux-x64
chmod +x code-server
./code-server -p 8443
