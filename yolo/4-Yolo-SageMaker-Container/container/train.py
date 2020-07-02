
import sys
import os  
import shutil
import subprocess

train_bash_command_template = "darknet detector train {} {} {}  -dont_show" 
predict_bash_command_template = "darknet detector test {} {} {} {} -dont_show" 

def train():
    coco_cfg_sg_path = "/opt/ml/input/data/dinfo/obj.data"
    yolov4_cfg_sg_path = "/opt/ml/input/data/cfg/custom-yolov4-detector.cfg" 
    weight_sg_path = "/opt/ml/input/data/yolo_model/yolov4.conv.137"
    train_local(coco_cfg_sg_path, yolov4_cfg_sg_path, weight_sg_path)
    if os.path.isfile('backup/custom-yolov4-detector_final.weights'):
        shutil.copyfile('backup/custom-yolov4-detector_final.weights', '/opt/ml/model/custom-yolov4-detector_final.weights')

def mk_dir(sub_dir, working_dir=None):
    output_path = None 
    if working_dir: 
        output_path = working_dir+'/'+sub_dir
    else: 
        output_path = sub_dir 
    if not os.path.exists(output_path):
        os.mkdir(output_path) 

def train_local(coco_cfg, yolov4_cfg, weights, working_dir=None):
    mk_dir('backup', working_dir)
    train_bash_command = train_bash_command_template.format(coco_cfg, yolov4_cfg, weights)
    process = subprocess.Popen(train_bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output, error)
   

def predict_local(coco_cfg, yolov4_cfg, weights, test_file, working_dir):
    bash_command = predict_bash_command_template.format(coco_cfg, yolov4_cfg, weights, test_file)
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    if os.path.isfile('predictions.jpg'):
        shutil.copyfile('predictions.jpg', working_dir+'/predictions.jpg')
    print(output, error)
   

if __name__ == "__main__":
    if (sys.argv[1] == "train"):
        train()
    elif (sys.argv[1]=="train_local"):
        coco_cfg = sys.argv[2]   
        yolov4_cfg = sys.argv[3]
        weight = sys.argv[4]
        working_dir = sys.argv[5]
        train_local(coco_cfg, yolov4_cfg, weight, working_dir)
    elif (sys.argv[1]=="predict_local"):
        coco_cfg = sys.argv[2]   
        yolov4_cfg = sys.argv[3]
        weight = sys.argv[4]
        test_file = sys.argv[5]
        working_dir = sys.argv[6]
        predict_local(coco_cfg, yolov4_cfg, weight, test_file, working_dir)
    else:
        print("Missing required argument 'train, traing_local or predict_local'.", file=sys.stderr)
        sys.exit(1)


