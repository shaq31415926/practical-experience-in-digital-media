import segno

qrcode = segno.make_qr("Hello, World")
# use the to_pil method to format the qr code this time
qrcode_rotated = qrcode.to_pil(
                light="lightblue",
                dark="green",
                scale=5
).rotate(45, expand=True) # expand = True expands the qr code
qrcode_rotated.save("images/rotated_qrcode.png")

