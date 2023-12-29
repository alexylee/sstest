from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep

def show(img):
    from PIL import Image, ImageDraw
    from ST7789 import ST7789
    canvas = Image.new('RGB', (240, 240))
    disp = ST7789()
    canvas.paste(img)
    disp.ShowImage(canvas, 0, 0)


camera = PiCamera(resolution=(240, 240), framerate=24)
rawCapture = PiRGBArray(camera, size=(240, 240))

i = 0
for stream in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
    print('frame#', i)
    frame = stream.array
    show(frame)
    rawCapture.truncate(0)
    sleep(1)
    i = i + 1
    if (i > 10):
        break

rawCapture.close()
camera.close()