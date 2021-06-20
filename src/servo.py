import RPi.GPIO as GPIO
import time

servoPIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

T = 5

try:
  while True:
    p.ChangeDutyCycle(2.5)
    print(2.5)
    time.sleep(T)
    p.ChangeDutyCycle(10)
    print(10)
    time.sleep(T)
    p.ChangeDutyCycle(12.5)
    print(12.5)
    time.sleep(T)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
