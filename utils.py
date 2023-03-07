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
    clearCache: clear Cache;
@para:
    cap: video;
'''

def clearCache(cap):
        cap.release()
        cv2.destroyAllWindows()
        
        motor_l1.stop()
        motor_l2.stop()
        motor_r1.stop()
        motor_r2.stop()
        GPIO.cleanup()