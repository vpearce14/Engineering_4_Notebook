from gpiozero import MotionSensor
from picamera import PiCamera, Color
sense = MotionSensor(4)
mycamera = PiCamera()
from time import sleep
while True:
    sense.wait_for_motion()
    print("Motion detected!")
    mycamera.start_preview(fullscreen=False,window=(100,200,300,400))
    sense.wait_for_no_motion()
    mycamera.stop_preview()
