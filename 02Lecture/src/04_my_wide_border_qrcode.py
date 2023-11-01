import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("../images/my_wide_border_qrcode.png",
            scale=5,
            border=10)