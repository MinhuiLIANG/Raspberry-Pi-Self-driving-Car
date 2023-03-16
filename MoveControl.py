import RPi.GPIO as GPIO 
import cv2

GPIO.setwarnings(False)

# Set the GPIO port to BCM number specification
GPIO.setmode(GPIO.BCM)

# Pins
INT2 = 18                   
INT1 = 23                  
INT4 = 24                   
INT3 = 25                   

# Pins to OUTPUT
GPIO.setup(INT1, GPIO.OUT)
GPIO.setup(INT2, GPIO.OUT)
GPIO.setup(INT3, GPIO.OUT)
GPIO.setup(INT4, GPIO.OUT)

# Set PWM frequency
motor_l1 = GPIO.PWM(INT1, 500)  
motor_l2 = GPIO.PWM(INT2, 500) 
motor_r1 = GPIO.PWM(INT3, 500)   
motor_r2 = GPIO.PWM(INT4, 500)   

# init
motor_l1.start(0)   
motor_l2.start(0)   
motor_r1.start(0)   
motor_r2.start(0)  

'''
@func: 
    left: car turn left;
    right: car turn right;
    forward: car move forward;
    move_pid: car move under pid control.
    
@para:
    speed: speed of car;
    speed1, speed2: speed of car under pid control.
'''

def left(speed):
        motor_l1.ChangeDutyCycle(0)     
        motor_l2.ChangeDutyCycle(0)
        motor_r1.ChangeDutyCycle(0)
        motor_r2.ChangeDutyCycle(speed)

def right(speed):
        motor_l1.ChangeDutyCycle(0)     
        motor_l2.ChangeDutyCycle(speed)
        motor_r1.ChangeDutyCycle(0)
        motor_r2.ChangeDutyCycle(0)

def forward(speed):
        motor_l1.ChangeDutyCycle(0)    
        motor_l2.ChangeDutyCycle(speed)
        motor_r1.ChangeDutyCycle(0)
        motor_r2.ChangeDutyCycle(speed)

def move_pid(speed1,speed2):
    motor_l1.ChangeDutyCycle(0)     
    motor_l2.ChangeDutyCycle(speed1)
    motor_r1.ChangeDutyCycle(0)
    motor_r2.ChangeDutyCycle(speed2)
