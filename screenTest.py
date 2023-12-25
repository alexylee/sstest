from PIL import Image, ImageDraw

from ST7789 import ST7789

canvas = Image.new('RGB', (240, 240))
disp = ST7789()

img = Image.open('btc2.png')
canvas.paste(img)

disp.ShowImage(canvas, 0, 0)