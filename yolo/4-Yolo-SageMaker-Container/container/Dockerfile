# SageMaker PyTorch image
#FROM 520713654638.dkr.ecr.us-west-2.amazonaws.com/sagemaker-pytorch:1.4.0-gpu-py3
FROM 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-training:1.5.0-gpu-py36-cu101-ubuntu16.04

ENV PATH="/opt/ml/code:${PATH}"

# /opt/ml and all subdirectories are utilized by SageMaker, we use the /code subdirectory to store our user code.
#COPY /darknet /opt/ml/code

# this environment variable is used by the SageMaker PyTorch container to determine our user code directory.
#ENV SAGEMAKER_SUBMIT_DIRECTORY /opt/ml/code

# this environment variable is used by the SageMaker PyTorch container to determine our program entry point
# for training and serving.
# For more information: https://github.com/aws/sagemaker-pytorch-container
#ENV SAGEMAKER_PROGRAM cifar10.py
