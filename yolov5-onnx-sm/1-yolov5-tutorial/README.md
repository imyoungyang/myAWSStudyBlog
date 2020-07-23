# Installation

```
source activate pytorch_p36
git clone https://github.com/ultralytics/yolov5 # clone repo
python3 -c "from yolov5.utils.google_utils import gdrive_download; gdrive_download('1n_oKgR81BJtqk75b00eAjdv03qVCQn2f','coco128.zip')" # download dataset
cd yolov5
./weights/download_weights.sh # download weights

# detection
python detect.py --weights yolov5s.pt --img 416 --conf 0.4 --source ./inference/images/
```

# Container way

```
sudo docker pull ultralytics/yolov5:latest
sudo docker run --gpus all --ipc=host -it ultralytics/yolov5:latest
python3 detect.py
```