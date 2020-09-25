#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:52:56 2020

@author: rampfire
"""


import os
import cv2

for image in os.listdir("/home/rampfire/tom_yolo/YoloV3/data/customdata/images"):
    
#    print("./data/customdata/images/"+image)
    temp=cv2.imread("/home/rampfire/tom_yolo/YoloV3/data/customdata/images/"+image)
    
    print(temp.shape[0],temp.shape[1])
    
#    ./data/customdata/images/img001.jpg
    
    
#temp=cv2.imread("/home/rampfire/tom_yolo/YoloV3/data/customdata/images/"+image)
#    
#temp.shape[:2]
#    