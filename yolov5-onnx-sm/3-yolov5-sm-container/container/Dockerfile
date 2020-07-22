#ARG BASE_IMG=763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:1.5.1-gpu-py36-cu101-ubuntu16.04
ARG BASE_IMG=${BASE_IMG}
FROM ${BASE_IMG} 

ENV PATH="/opt/code:${PATH}"

RUN apt-get update \
 && apt-get install -y --no-install-recommends --allow-unauthenticated \
    jq

## fix /usr/local/cuda-10.0/compat/libcuda.so
RUN bash -c 'echo "/usr/local/cuda-10.0/compat" > /etc/ld.so.conf.d/cuda.conf'
RUN ldconfig -v

RUN cd opt && git clone https://github.com/ultralytics/yolov5
RUN pip install -r /opt/yolov5/requirements.txt

ENV PATH="/opt/yolov5:${PATH}"
WORKDIR /opt/code

COPY train /opt/code
COPY serve /opt/code
