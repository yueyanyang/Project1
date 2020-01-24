#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:21:38 2020

@author: jacobksu
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt



def rescale_frame(frame, percent=70):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def split_video_channels(mirror=False):
 
    cap = cv2.VideoCapture('live_camera.avi') 
#    cv2.namedWindow('Webcam Life2Coding',cv2.WINDOW_NORMAL)
#    zeros = None
    while True:
        ret_val, frame = cap.read()
        if ret_val == True:
            if mirror:
                #flip the image
                frame = cv2.flip(frame, 1)
 
                       # The OpenCV image sequence is Blue(B),Green(G) and Red(R)
            
            frame[: , : ,2]=0.5
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hsv = rescale_frame(hsv, percent=70)
            cv2.imshow('hsv',hsv)
            
            
            
            hist = cv2.calcHist( hsv, [1], None, [256], [0, 256] )
            plt.plot(hist)
            plt.show()
            
            
            
            
            
            
        else:
            break
 
        if cv2.waitKey(1) & 0xFF == ord('q'):  # if 'q' is pressed then quit
            break
    cap.release()
    cv2.destroyAllWindows()
 
def main():
    split_video_channels(mirror=True)
    
if __name__ == '__main__':
    main()