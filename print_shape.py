#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:52:47 2020

@author: jacobksu
"""
import numpy as np
import cv2

cap = cv2.VideoCapture('live_camera.avi')



while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        print(frame.shape)

        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
           
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
