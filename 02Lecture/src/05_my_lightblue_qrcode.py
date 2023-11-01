import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("../images/my_lightblue_qrcode.png",
            light="#ADD8E6",
            scale=5)