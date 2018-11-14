from picamera import PiCamera, Color
from time import sleep

myCamera = PiCamera()

myCamera.start_preview(fullscreen=False,window=(100,200,300,400))
myCamera.start_recording('myvid.h264')
sleep(10)
myCamera.stop_recording()
myCamera.stop_preview()
