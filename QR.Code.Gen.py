"""
Dependencies:
pyqrcode
pypng
pillow for PIL importing image
i.e pip install pyqrcode 
    pip install pypng
    pip install pillow
"""
import pyqrcode
from PIL import Image
link = input("Enter anything to generate QR :")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=10)
Image.open("QRCode.png")
