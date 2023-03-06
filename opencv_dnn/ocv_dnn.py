import cv2
import numpy as np

with open('classification_classes_ILSVRC2012.txt') as f:
    image_set_names = f.read().split('\n')
    
class_names = [name.split(',')[0] for name in image_net_names]
