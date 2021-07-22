# bla


import RPi.GPIO as GPIO
import time

def RunPump(runTime):
    servoPIN = 12
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    p.ChangeDutyCycle(12.5)
    print(12.5)
    time.sleep(runTime)

    p.stop()
    GPIO.cleanup()



servoPIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
p.ChangeDutyCycle(12.5)
print(12.5)
time.sleep(runTime)

p.stop()
GPIO.cleanup()
