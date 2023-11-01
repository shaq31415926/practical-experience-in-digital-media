import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("../images/my_green_datadark_qrcode.png",
            scale=5,
            light="lightblue",
            dark="darkblue",
            data_dark="green")

qrcode.save("../images/my_green_datamodules_qrcode.png",
            scale=5,
            light="lightblue",
            dark="darkblue",
            data_dark="green",
            data_light="lightgreen")