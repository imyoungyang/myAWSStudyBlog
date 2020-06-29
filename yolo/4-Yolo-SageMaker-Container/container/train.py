
import sys
import os  
import shutil

#bashCommand_template = "darknet detector train /opt/ml/input/data/cfg/coco.data /opt/ml/input/data/cfg/yolov4.cfg /opt/ml/input/data/yolo_model/csdarknet53-omega_final.weights -dont_show" 
bashCommand_template = "darknet detector train {} {} {}  -dont_show" 
predict_bashCommand_template = "darknet detector test {} {} {} {} -dont_show" 

def train():
    coco_cfg_sg_path = "/opt/ml/input/data/dinfo/obj.data"
    yolov4_cfg_sg_path = "/opt/ml/input/data/cfg/custom-yolov4-detector.cfg" 
    #weight_sg_path = "/opt/ml/input/data/yolo_model/csdarknet53-omega_final.weights"
    weight_sg_path = "/opt/ml/input/data/yolo_model/yolov4.conv.137"
    train_local(coco_cfg_sg_path, yolov4_cfg_sg_path, weight_sg_path)
    if os.path.isfile('backup/yolov4_final.weights'):
        shutil.copyfile('backup/yolov4_final.weights', '/opt/ml/model/yolov4_final.weights')

def train_local(coco_cfg, yolov4_cfg, weights):
    
    os.mkdir('backup')
    bashCommand = bashCommand_template.format(coco_cfg, yolov4_cfg, weights)
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output, error)
   

def predict_local(coco_cfg, yolov4_cfg, weights, test_file, working_dir):
    
    os.mkdir('backup')
    bashCommand = predict_bashCommand_template.format(coco_cfg, yolov4_cfg, weights, test_file)
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
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
        train_local(coco_cfg, yolov4_cfg, weight)
    elif (sys.argv[1]=="predict_local"):
        coco_cfg = sys.argv[2]   
        yolov4_cfg = sys.argv[3]
        weight = sys.argv[4]
        test_file = sys.argv[5]
        working_dir = sys.argv[6]
        predict_local(coco_cfg, yolov4_cfg, weight, test_file, working_dir)
    else:
        print("Missing required argument 'train'.", file=sys.stderr)
        sys.exit(1)


