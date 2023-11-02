import segno

qrcode = segno.make_qr("HELLO WORLD!!")
qrcode.save("images/basic_qrcode.png")