from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
from io import BytesIO
from PIL import Image

def show(img):
    from PIL import Image, ImageDraw
    from ST7789 import ST7789
    canvas = Image.new('RGB', (240, 240))
    disp = ST7789()
    canvas.paste(img)
    disp.ShowImage(canvas, 0, 0)


camera = PiCamera(resolution=(240, 240), framerate=24)
stream = BytesIO()

i = 0
for s in camera.capture_continuous(stream, format="jpeg", use_video_port=True):
    print('frame#', i)
    stream.seek(0)
    img = Image.open(stream)
    show(img)
    sleep(1)
    stream.seek(0)
    stream.truncate()
    i = i + 1
    if (i > 10):
        break

camera.close()