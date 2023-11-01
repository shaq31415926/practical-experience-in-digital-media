import segno

qrcode = segno.make_qr("Hello, World")

qrcode_rotated = qrcode.to_pil().rotate(45)
qrcode_rotated.save("../images/my_rotated_qrcode.png")

qrcode = segno.make_qr("Hello, World")

qrcode_rotated = qrcode.to_pil().rotate(45, expand=True)
qrcode_rotated.save("../images/my_rotated_qrcode2.png")