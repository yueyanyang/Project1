#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:01:03 2020

@author: jacobksu
"""

import cv2

capture = cv2.VideoCapture('live_camera.avi')
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print('Frame count:', frame_count)

def print_capture_properties(*args):
    capture = cv2.VideoCapture(*args)
    print('Created capture:', *args)
    print('Frame count:', int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    print('Frame width:', int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame rate:', capture.get(cv2.CAP_PROP_FPS))
    print('\n')
    
print_capture_properties('live_camera.avi')
