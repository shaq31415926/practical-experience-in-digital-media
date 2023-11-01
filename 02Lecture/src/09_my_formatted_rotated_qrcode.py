import segno

qrcode = segno.make_qr("Hello, World")

qrcode_rotated = qrcode.to_pil(scale=5,
                               light="lightblue",
                               separator="pink",
                               # quiet_zone="red",
                               dark="green"
                               ).rotate(45, expand=True)
qrcode_rotated.save("../images/my_formatted_rotated_qrcode.png",

                    )