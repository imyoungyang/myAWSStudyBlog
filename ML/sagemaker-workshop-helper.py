# Download and Test Images
# Bird
!wget -O /tmp/test.jpg https://upload.wikimedia.org/wikipedia/commons/1/17/Rotkehlchen_bird.jpg
file_name = '/tmp/test.jpg'
from IPython.display import Image
Image(file_name)

# Image resizing and paste into center.
from matplotlib.pyplot import imshow
from PIL import Image
import numpy as np

%matplotlib inline

desired_size = 32
im = Image.open(file_name)
old_size = im.size

ratio = float(desired_size)/max(old_size)
new_size = tuple([int(x*ratio) for x in old_size])

new_size

im = im.resize(new_size, Image.ANTIALIAS)
np_im = np.array(im)
np_im.shape

new_im = Image.new("RGB", (desired_size, desired_size))
new_im.paste(im, ((desired_size-new_size[0])//2,
                    (desired_size-new_size[1])//2))

np_new_im = np.array(new_im)
np_new_im.shape

imshow(np_new_im)

# Simple way to resize image example
size = 32, 32
im.resize(size, Image.ANTIALIAS)

np_im = np.array(im)
np_im.shape

imshow(np_im)

# Image reshape for keras tf input 1x4
np_new_im = np_new_im[np.newaxis, ...]
np_new_im.shape

# predict inference
response = predictor.predict({'inputs_input': np_new_im})
response

# predict with existing endpoint
import json
from sagemaker.tensorflow import TensorFlowPredictor
predictor = TensorFlowPredictor('sagemaker-tensorflow-2019-07-17-03-09-42-707')
result = predictor.predict({'inputs_input': np_new_im})

# Cifar 10 class
# 0 : airplane
# 1 : automobile
# 2 : bird
# 3 : cat
# 4 : deer
# 5 : dog
# 6 : frog
# 7 : horse
# 8 : ship
# 9 : truck
object_categories = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
print(object_categories[int(predict_class)])