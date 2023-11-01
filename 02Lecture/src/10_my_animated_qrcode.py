import segno
from urllib.request import urlopen

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
slts_qrcode.to_artistic(background=nirvana_url,
                        target="../images/my_animated_qrcode.gif",
                        light="blue",
                        scale=5)