#!/bin/bash
image=$1
if [ "$image" == "" ]
then
    echo "Usage: $0 <image-name>"
    exit 1
fi
account=$(aws sts get-caller-identity --query Account --output text)
region=$(aws configure get region)
fullname="${account}.dkr.ecr.${region}.amazonaws.com/${image}:latest"

aws ecr describe-repositories --repository-names "${image}" > /dev/null 2>&1

if [ $? -ne 0 ]
then
    aws ecr create-repository --repository-name "${image}" > /dev/null
fi

$(aws ecr get-login --region ${region} --no-include-email)
$(aws ecr get-login --registry-ids 763104351884 --region ${region} --no-include-email)
base_img='763104351884.dkr.ecr.'$region'.amazonaws.com/pytorch-training:1.5.1-gpu-py36-cu101-ubuntu16.04'
echo 'base_img:'$base_img

cd container
docker build -t ${image} -f Dockerfile --build-arg BASE_IMG=$base_img .
docker tag ${image} ${fullname}

docker push ${fullname}
