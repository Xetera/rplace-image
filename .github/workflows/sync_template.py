from PIL import Image
import requests
from io import BytesIO

with open("./reference.png") as file:
    img = Image.open(file.buffer)
    img = img.resize((img.size[0], img.size[1]), Image.NEAREST)

    mask_url = "https://media.discordapp.net/attachments/267492253168173056/959625681141104700/mask.png"
    response = requests.get(mask_url)
    mask_i = Image.open(BytesIO(response.content))
    mask = Image.new("1", (2000, 1000), 0)
    mask.paste(mask_i)

    tl = (1607, 880) # top left corner

    final_img = Image.new('RGBA', (2000, 1000))
    unmasked_img = Image.new('RGBA', (2000, 1000))
    unmasked_img.paste(img, tl)
    final_img = Image.composite(final_img, unmasked_img, mask)
    final_img.save("red_velvet_overlay.png")

