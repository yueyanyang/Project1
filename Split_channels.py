#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:00:46 2020

@author: jacobksu
"""

import cv2
import numpy as np
 
def split_video_channels(mirror=False):
 
    cap = cv2.VideoCapture('live_camera.avi')
    cv2.namedWindow('Webcam Life2Coding',cv2.WINDOW_NORMAL)
    zeros = None
    while True:
        ret_val, frame = cap.read()
 
        if ret_val == True:
            if mirror:
                #flip the image
                frame = cv2.flip(frame, 1)
 
            # split the image into its RGB channels
            height, width, layers = frame.shape
            zeroImgMatrix = np.zeros((height, width), dtype="uint8")
 
            # The OpenCV image sequence is Blue(B),Green(G) and Red(R)
            (B, G, R) = cv2.split(frame)
 
            # we would like to construct a 3 channel Image with only 1 channel filled
            # and other two channels will be filled with zeros
            B = cv2.merge([B, zeroImgMatrix, zeroImgMatrix])
            G = cv2.merge([zeroImgMatrix, G, zeroImgMatrix])
            R = cv2.merge([zeroImgMatrix, zeroImgMatrix, R])
 
 
            #we would like to show the 4 images like ( Original | Blue
            #                                          Green    | Red  )
 
            # so we need to double the image size as it will be 4 times the original image
            final = np.zeros((height * 2, width * 2, 3), dtype="uint8")
 
#            final[0:height, 0:width] = frame # 1st Quarter=original
#            final[0:height, width:width * 2] = B # 2nd Quarter= Blue
#            final[height:height * 2, 0:width] = G   # 3rd Quarter= Red
#            final[height:height * 2, width:width * 2] = R  # 4th Quarter= Green
 
            cv2.imshow('Webcam Life2Coding', B)
            cv2.imshow('G',G)
            cv2.imshow('R',R)
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
