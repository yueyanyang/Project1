# -*- coding: utf-8 -*-
import numpy as np
import cv2
import time

capture_duration = 450

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
    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed Esc')
        break            
capture.release()
video.release()
cv2.destroyAllWindows()

capture = cv2.VideoCapture('live_camera.avi')
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print('Frame count:', frame_count)



