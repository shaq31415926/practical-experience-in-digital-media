import segno
from urllib.request import urlopen

# create a qr code object with a youtube link
slts = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
# open the link of the giphy which you want to use to animate your qr code
nirvana_url = urlopen("https://media.giphy.com/media/lqPZLGWcXJHS21kubp/giphy.gif")

# use the to_artistic method to replace the background with the url and save as an image of your choice
slts.to_artistic(
    background=nirvana_url,
    target="images/animated_qrcode.gif",
    scale=5
)
