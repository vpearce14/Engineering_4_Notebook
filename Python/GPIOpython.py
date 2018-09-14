import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
for i in range(0,10):
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    sleep(0.5)
GPIO.cleanup()
