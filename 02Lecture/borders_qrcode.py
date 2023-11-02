import segno

qrcode = segno.make_qr("hello world")
# to remove the quiet zone
qrcode.save("images/borderless_qrcode.png",
            scale=10,
            border=0
            )

# to increase the size of the qr code
qrcode.save("images/wide_qrcode.png",
            scale=10,
            border=10
            )