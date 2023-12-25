from PIL import Image, ImageDraw, ImageFont

im = Image.open('btc2.png')
draw = ImageDraw.Draw(im)

font = ImageFont.truetype("NotoSerifKR-Regular.otf", 24)
draw.text((30, 30), "TEST: 한글 테스트", (255,255,255), font)
 
im.save('btc2text.png')
