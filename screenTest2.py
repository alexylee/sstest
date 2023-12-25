from PIL import Image, ImageDraw, ImageFont

from ST7789 import ST7789

canvas = Image.new('RGB', (240, 240))
disp = ST7789()

img = Image.open('btc2.png')
canvas.paste(img)

draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype("NotoSerifKR-Regular.otf", 24)
draw.text((30, 30), "TEST: 한글 테스트", (255,255,255), font)

disp.ShowImage(canvas, 0, 0)