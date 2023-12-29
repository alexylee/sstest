from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (240, 240)
camera.framerate = 24

camera.start_preview()
sleep(2) # wait for camera starting

camera.capture('test.jpg')   # save to file and automatically close 