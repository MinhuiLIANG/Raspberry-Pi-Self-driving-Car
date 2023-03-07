import RPi.GPIO as GPIO
import time
import cv2
import numpy as np

from KmeansClassifier import k_mean_two
from MoveControl import forward, left, right
from ImgProcess import cvAlgorithm
from Utils import clearCache

state=0
column_threshold = 5   

cap = cv2.VideoCapture(0)
while (1):
    dst = cvAlgorithm(cap)

    color = dst[420][column_threshold:641-column_threshold]
    black_count = np.sum(color == 0)
    black_index = np.array([i for i,x in enumerate(color) if x==0])
    
    center1,center2,class_result=k_mean_two(black_index, 100, 3)

    if black_count != 0:
        if class_result == 1:
            if black_index[0] >= 300:
                center1 = 0
            else:
                center2 = 640
        center = (center1 + center2) / 2
        direction_error = center-len(color)/2

        if direction_error > 30:
            print('turning left')
            right(65)
            state=1
        elif direction_error < -30:
            print('turning right')
            left(65)
            state=2
        else:
            print('going forward')
            forward(35)
            state=3
    else:
        if state==1:
            print('turning left')
            right(65)
        elif state==2:
            print('turning right')
            left(65)
        elif state==3:
            print('going forward')
            forward(35)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

clearCache(cap)
