#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:21:38 2020

@author: jacobksu
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

#import capture_vid

cap = cv2.VideoCapture('live_camera.avi')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
video = cv2.VideoWriter('/home/jacobksu/Insync/jburne35@students.kennesaw.edu/OneDrive Biz/SPRING 2020/Machine Learning/Proj1/modified_video.avi', cv2.VideoWriter_fourcc('M','J','P','G'),
                        30, (frame_width, frame_height))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

def capture_vid():
    capture_duration = 450  # seconds
    
    capture = cv2.VideoCapture(0)
    frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('Frame width:', frame_width)
    print('Frame height:', frame_height)
    
    video = cv2.VideoWriter('/home/jacobksu/Insync/jburne35@students.kennesaw.edu/OneDrive Biz/SPRING 2020/Machine Learning/Proj1/live_camera.avi', cv2.VideoWriter_fourcc('M','J','P','G'),
                            30, (frame_width, frame_height))
    start_time = time.time()
    while( int(time.time() - start_time) < capture_duration ):
        has_frame, frame = capture.read()
        if not has_frame:
            print('Can\'t get frame')
            break
            
        video.write(frame)
            
        cv2.imshow('frame', frame)
    
capture_vid()
    
def print_capture_properties(*args):
    capture = cv2.VideoCapture(*args)
    print('Created capture:', args)
    print('Frame count:', int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    print('Frame width:', int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame rate:', capture.get(cv2.CAP_PROP_FPS))
    print('\n')
    
print_capture_properties('live_camera.avi')


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
 
     # The OpenCV image sequence is Blue(B),Green(G) and Red(R) AND RESCALE
                (B, G, R) = cv2.split(frame)
                B = rescale_frame(B, percent=70)
                G = rescale_frame(G, percent=70)
                R = rescale_frame(R, percent=70)
                
                cv2.imshow('B',B)
                cv2.imshow('G',G)
                cv2.imshow('R',R)
                
      ## V values, Histogram,           
                frame[: , : ,2]=0.5
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                hsv = rescale_frame(hsv, percent=70)
#                cv2.imshow('hsv',hsv)
               
            
            

            hist, bins = np.histogram(hsv,256, [0,255])
            plt.subplot(2,1,1)
            plt.fill_between(range(256), hist, 0)
            plt.xlabel('S Histogram')
            plt.show()
           
            hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
            hist_S, bins = np.histogram(hsv[..., 2], 256, [0, 255])
            plt.subplot(2,1,2)
            plt.fill_between(range(256),hist_S,0)
            plt.xlabel('Equalized S HIstogram')
            plt.show()
#            hsv_eq = cv2.equalizeHist(hsv)
            
        ## Gaussuian 
            color_eq = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            gauss_blur = cv2.GaussianBlur(color_eq, (7, 7), 0)
            cv2.imshow('Filtered Image',gauss_blur)
            video.write(gauss_blur)
            
           
        else:
            break
            
        
    
        if cv2.waitKey(1) & 0xFF == ord('q'):  # if 'q' is pressed then quit
            break
        
    
    cap.release()
    cv2.destroyAllWindows()
    
def modified_vid():
    cap = cv2.VideoCapture('modified_video.avi')
    while True:
        ret_val, frame = cap.read()
        if ret_val == True:
            frame = cv2.flip(frame, 1)
            cv2.imshow('MODIFIED VIDEO',frame)
        
    modified_vid()

def main():
    split_video_channels(mirror=True)
    
if __name__ == '__main__':
    main()
    
