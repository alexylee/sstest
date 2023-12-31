from PIL import Image

## add missing dependancies:
## 1) https://pypi.org/project/pyzbar/#files
## 2) download pyzbar-0.1.9-py2.py3-none-win_amd64.whl 
## 3) unzip with 7-zip 
## 4) copy lib*.dll to C:\py.envs\seedsigner-env\Lib\site-packages\pyzbar
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol

img = Image.open('qr1.png')
barcodes = pyzbar.decode(img, symbols=[ZBarSymbol.QRCODE], binary=False)

for barcode in barcodes:
    # Only pull and return the first barcode
    qr = barcode.data
    break

print('QR: ', qr)
