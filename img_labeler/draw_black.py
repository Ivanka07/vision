#!/bin/python

import numpy as np
import cv2

dir = '/home/ivanna/fa_data/images_0/'
write_dir = '/home/ivanna/fa_data/images_1/'

for i in range(4029, 4030):
    print('i ' + str(i))
    path = dir + str(i) +'.png'
    img = cv2.imread(path)
    cv2.rectangle(img, (10, 230), (260, 540), (0, 0, 0), -1)
    wpath = dir + str(i) + '.png'
    cv2.imwrite(wpath,img)
