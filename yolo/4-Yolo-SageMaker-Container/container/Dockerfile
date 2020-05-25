# SageMaker PyTorch image
FROM 763104351884.dkr.ecr.us-west-2.amazonaws.com/tensorflow-training:1.15.2-gpu-py36-cu100-ubuntu18.04

ENV PATH="/opt/ml/code:${PATH}"

## install cmake 3.17 && opencv
RUN apt-get remove cmake
RUN apt-get update \
 && apt-get install -y --no-install-recommends --allow-unauthenticated \
    python3-opencv
RUN curl -sSL https://github.com/Kitware/CMake/releases/download/v3.17.2/cmake-3.17.2-Linux-x86_64.tar.gz | tar -xzC /opt
RUN mv /opt/cmake-3.17.2-Linux-x86_64 /opt/cmake
RUN ln -s /opt/cmake/bin/cmake /usr/bin/cmake

## fix /usr/local/cuda-10.0/compat/libcuda.so
RUN bash -c 'echo "/usr/local/cuda-10.0/compat" > /etc/ld.so.conf.d/cuda.conf'
RUN ldconfig -v

## Build darknet
RUN cd opt && git clone https://github.com/AlexeyAB/darknet
RUN cd /opt/darknet && ./build.sh

ENV PATH="/opt/darknet:${PATH}"
WORKDIR /opt/darknet

# /opt/ml and all subdirectories are utilized by SageMaker, we use the /code subdirectory to store our user code.
#COPY /darknet /opt/ml/code

# this environment variable is used by the SageMaker PyTorch container to determine our user code directory.
#ENV SAGEMAKER_SUBMIT_DIRECTORY /opt/ml/code

# this environment variable is used by the SageMaker PyTorch container to determine our program entry point
# for training and serving.
# For more information: https://github.com/aws/sagemaker-pytorch-container
#ENV SAGEMAKER_PROGRAM cifar10.py
