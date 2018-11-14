import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN)
GPIO.output(17,GPIO.LOW)
while True:
    inputt = GPIO.input(18)
    print(inputt)
    if inputt:
        GPIO.output(17,GPIO.HIGH)
    else:
        GPIO.output(17,GPIO.LOW)
GPIO.cleanup()
