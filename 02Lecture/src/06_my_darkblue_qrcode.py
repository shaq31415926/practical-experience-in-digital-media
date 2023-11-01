import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("../images/my_darkblue_qrcode.png",
            scale=5,
            dark="darkblue")

qrcode.save("../images/my_darkblue_qrcode2.png",
            scale=5,
            dark="darkblue",
            quiet_zone="maroon")