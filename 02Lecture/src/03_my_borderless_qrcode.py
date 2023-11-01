import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("../images/my_borderless_qrcode1.png",
            scale=5,
            border=0)
