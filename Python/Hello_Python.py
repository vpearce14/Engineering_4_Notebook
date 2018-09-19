import PPi.GPIO as GPIO
from time import sleep

gpio mode 0 out
gpio mode 1 out
for i in range (0,10):
    gpio write 0 1
    gpio write 1 1
    sleep 1
    gpio write 0 0
    gpio write 1 0
    sleep 1
