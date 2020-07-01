#!/bin/bash

region=$(aws configure get region)
$(aws ecr get-login --registry-ids 763104351884 --region ${region} --no-include-email)
base_img='763104351884.dkr.ecr.'$region'.amazonaws.com/tensorflow-training:1.15.2-gpu-py36-cu100-ubuntu18.04'
echo 'base_img:'$base_img
cd container
docker build -t yolov4 -f Dockerfile --build-arg BASE_IMG=$base_img .
