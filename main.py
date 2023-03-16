from Center_detection import GMM, K_means
from Image_process import cvAlgorithm
from MoveControl import forward, left, right
import RPi.GPIO as GPIO 
import time
import cv2
import numpy as np

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)  

INT2 = 18 
INT1 = 23 
INT4 = 24 
INT3 = 25 

GPIO.setup(INT1, GPIO.OUT)
GPIO.setup(INT2, GPIO.OUT)
GPIO.setup(INT3, GPIO.OUT)
GPIO.setup(INT4, GPIO.OUT)

motor_l1 = GPIO.PWM(INT1, 500) 
motor_l2 = GPIO.PWM(INT2, 500) 
motor_r1 = GPIO.PWM(INT3, 500) 
motor_r2 = GPIO.PWM(INT4, 500) 

motor_l1.start(0)
motor_l2.start(0) 
motor_r1.start(0) 
motor_r2.start(0) 

state = 3
column_threshold = 5
left_s = 25 
right_s = 25 
forward_s = 15 
threshold = 250 
first_line = 435
second_line = 450
left_threshold = 300
right_threshold = 340
error_threshold = 50
right_state = 1
left_state = 2
forward_state = 3
epoch_num = 3
width = 640

video_capture = cv2.VideoCapture(0)
while 1:

    dst, frame = cvAlgorithm(video_capture)

    cv2.imshow("dilate", dst)
    cv2.imshow("capture", frame)

    pixels = dst[first_line][column_threshold:width - 1 - column_threshold] 

    count = np.sum(pixels == 0)
    position = np.array([i for i, x in enumerate(pixels) if x == 0]) 
   
    center_1, center_2, res = GMM(position, threshold, epoch_num)
    #center_1, center_2, class_result = K_means(black_index, threshold, epoch_num)

    if count != 0:
        
        if res == 1:
            if position[-1] <= left_threshold: #car close to left line
                center_1 = center_2
                center_2 = width 
            elif position[0] >= right_threshold: #car close to right line
                center_2 = center_1
                center_1 = 0
            else:
                re_pixels = dst[second_line][column_threshold:width - 1 - column_threshold] 
                re_count = np.sum(re_pixels == 0)
                re_position = np.array([i for i, x in enumerate(re_pixels) if x == 0])
                if re_count != 0:
                    if re_position[0] < re_position[0]: 
                        center_2 = center_1
                        center_1 = 0
                    else:
                        center_1 = center_2
                        center_2 = width
                else:
                    center_1 = width/2
                    center_2 = width/2

        center = (center_1 + center_2) / 2 

        direction_error = center - len(pixels) / 2

        if res == 0:
            forward(forward_s)

        elif direction_error > error_threshold: 
            right(right_s)
            state = right_state
        elif direction_error < 0-error_threshold:
            left(left_s)
            state = left_state
        else:
            forward(forward_s)
            state = forward_state
    else:
        forward(forward_s)

video_capture.release()
cv2.destroyAllWindows()
motor_l1.stop()
motor_l2.stop()
motor_r1.stop()
motor_r2.stop()
GPIO.cleanup()