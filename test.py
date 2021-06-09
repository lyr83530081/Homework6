
import torch
import time
import pandas as pd
import cv2
import numpy as np
from PIL import Image
import torch
from efficientdet import EfficientDet
from nets.efficientdet import EfficientDetBackbone

from nets.efficientdet import EfficientDetBackbone
from nets.efficientnet import EfficientNet
import os

def ttt(image):
    pass

if __name__ == '__main__':
    efficientdet = EfficientDet(classes_path = 'model_data/new_classes.txt' )
    file_path = './data/test_images'
    classes_path = 'model_data/new_classes.txt'
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    label_list = [i+1 for i in range(len(class_names))]
    label_dict = dict(zip(class_names,label_list))
    image_filename = []
    label_id = []
    x = []
    y = []
    w = []
    h = []
    confidence = []



    list_dir = os.listdir(file_path)
    for dir_img in list_dir:

        image = Image.open(file_path+'/'+dir_img)

        r_image,info = efficientdet.detect_image(image)
        if info:
            for i in range(len(info)):
                info_temp = info[i]
                image_filename.append(dir_img)
                label_id.append(label_dict[info_temp[0]])
                confidence.append(info_temp[1])
                y.append(info_temp[2])
                x.append(info_temp[3])
                h.append(info_temp[4])
                w.append(info_temp[5])
        #r_image.show()

#    zw = list(map(lambda x: x[0]-x[1], zip(w, x)))
#    zh = list(map(lambda x: x[0]-x[1], zip(h, y)))
    data = pd.DataFrame()
    data['image_filename'] = image_filename
    data['label_id'] = label_id
    data['x'] = x
    data['y'] = y
    data['w'] = w
    data['h'] = h
    data['confidence'] = confidence
    data.to_csv(r"test5.csv",mode = 'a',index =False)