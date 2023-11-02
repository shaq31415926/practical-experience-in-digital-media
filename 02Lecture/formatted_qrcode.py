import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("images/lightblue_qrcode.png",
            light="lightblue",
            scale=10
            )

qrcode.save("images/darkblue_qrcode.png",
            light="lightblue",
            dark="darkblue",
            scale=10
            )

qrcode.save("images/maroon_qrcode.png",
            light="lightblue",
            dark="darkblue",
            quiet_zone="maroon",
            scale=10
            )

qrcode.save("images/datamodules_qrcode.png",
            light="lightblue",
            dark="darkblue",
            data_dark="darkgreen",
            data_light="lightgreen",
            scale=10
            )