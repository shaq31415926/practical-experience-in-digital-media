import segno

qrcode = segno.make_qr("hello world")
qrcode.save("images/scaled_qrcode.png",
            scale=50)