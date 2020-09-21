#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:23:01 2020

@author: rampfire
"""


import os
import cv2


src_paths=["/home/rampfire/Downloads/b8c899a5-9c26-4230-8110-f11f6e545af6",
           "/home/rampfire/Downloads/336431b7-4e52-4cdc-9178-f6db0ed0e7e5"]
dest_path="/home/rampfire/tom_jerry/data"
file_count=1
for src in src_paths:
    for src_image in os.listdir(src):
        try:
#            print(os.path.join(src,src_image))
            image=cv2.imread(os.path.join(src,src_image))
            destination_save_path=os.path.join(dest_path,("image_"+str(file_count)+".jpg"))
            cv2.imwrite(destination_save_path,image)
            file_count+=1
        except:
            print(os.path.join(src,src_image))

