import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=3,
)

ba = bytearray(b'\x01\x02\x03\x04\x01\x02\x03\x04\x01\x02\x03\x04\x01\x02\x03\x04')
qr.add_data(bytes(ba))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").resize((240*5,240*5)).convert('RGBA')

img.save('qr2.png')

cropimg = img.crop((0, 0, 240, 240))
cropimg.save('qrcrop2_1.png')

cropimg = img.crop((240*4, 0, 240*4+240, 240))
cropimg.save('qrcrop2_2.png')

