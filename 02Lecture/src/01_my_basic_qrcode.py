import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("../images/my_basic_qrcode.png")