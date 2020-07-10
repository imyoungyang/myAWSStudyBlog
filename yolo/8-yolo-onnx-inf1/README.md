# Installation Notes

1. Use AWS DLAMI ubuntu 18 and select inf1 instance
2. In the terminal, run the following scripts to create conda environment.

```
conda create --clone aws_neuron_pytorch_p36 --name yolov5_neuron
source activate yolov5_neuron
pip install opencv torchvision onnx --upgrade
pip install coremltools==4.0b1
```

3. Download yolov5 source code and run the export.py

```
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
./weights/download_weights.sh
export PYTHONPATH="$PWD"  # add path
python models/export.py --weights yolov5s.pt --img 640 --batch 1  # export
```

4. Some know issues on CoreML

https://github.com/ultralytics/yolov5/issues/315
https://github.com/ultralytics/yolov5/issues/251
