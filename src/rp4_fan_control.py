import RPi.GPIO as GPIO
import time

servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

try:
    while True:
        GPIO.output(servoPIN, 0)
        time.sleep(5)
        GPIO.output(servoPIN, 1)
        time.sleep(5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
