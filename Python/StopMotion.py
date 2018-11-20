from picamera import PiCamera, Color
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button
GPIO.setmode(GPIO.BCM)
frame = 1
button=Button(5)
mycamera = PiCamera()
mycamera.start_preview(fullscreen=False,window=(100,200,300,400))
while True:
    try:
        button.wait_for_press()
        mycamera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        print ('/home/pi/animation/frame%03d.jpg' % frame)
        frame+=1
    except KeyboardInterrupt:
        mycamera.stop_preview()
        break
    sleep(1)
