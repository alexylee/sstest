import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=3,
)
qr.add_data('0001000200030004000100020003000400010002000300040001000200030004')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").resize((240*5,240*5)).convert('RGBA')

img.save('qr1.png')

cropimg = img.crop((0, 0, 240, 240))
cropimg.save('qrcrop1_1.png')

cropimg = img.crop((240*4, 0, 240*4+240, 240))
cropimg.save('qrcrop1_2.png')

