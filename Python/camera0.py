from picamera import PiCamera, Color
from time import sleep

myCamera = PiCamera()
myCamera.image_effect = 'cartoon'
myCamera.start_preview(fullscreen=False,window=(100,200,300,400))
myCamera.capture('blur3.jpg')      
sleep(2)
myCamera.stop_preview()
