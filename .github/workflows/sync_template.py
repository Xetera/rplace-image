from PIL import Image
import requests
from io import BytesIO

with open("./reference.png") as file:
    img = Image.open(file.buffer)
    img = img.resize((img.size[0] * 6, img.size[1] * 6), Image.NEAREST)

    mask_url = "https://media.discordapp.net/attachments/267492253168173056/959625681141104700/mask.png"
    response = requests.get(mask_url)
    mask_i = Image.open(BytesIO(response.content))
    mask = Image.new("1", (6000, 3000), 0)
    mask.paste(mask_i)

    tl = (1607 * 3, 880  * 3) # top left corner

    final_img = Image.new('RGBA', (6000, 3000))
    unmasked_img = Image.new('RGBA', (6000, 3000))
    unmasked_img.paste(img, tl)
    final_img = Image.composite(final_img, unmasked_img, mask)
    final_img.save("red_velvet_overlay.png")

