from PIL import Image
import requests
from io import BytesIO

SCALING = 3

def get_image(path, scaling = SCALING):
    with open(path) as file:
        img = Image.open(file.buffer)
        return img.resize((img.size[0] * scaling, img.size[1] * scaling), Image.NEAREST)

with open("./reference.png") as file:
    img = get_image("./reference.png")
    reve_girl_img = get_image("./reve-girl-reference.png")

    mask_url = "https://media.discordapp.net/attachments/267492253168173056/959625681141104700/mask.png"
    response = requests.get(mask_url)
    mask_i = Image.open(BytesIO(response.content))
    mask = Image.new("1", (2000 * SCALING, 2000 * SCALING), 0)
    large_mask = Image.new("1", (2000 * SCALING, 2000 * SCALING), 0)
    mask.resize((mask_i.size[0], mask_i.size[1] * 2), Image.NEAREST)
    mask.paste(mask_i, (0, 0))
    mask.paste(mask_i, (mask_i.width, 0))
    mask.paste(mask_i, (0, mask_i.height))
    mask.paste(mask_i, (mask_i.width, mask_i.height))

    tl = (1606 * SCALING, 879 * SCALING) # top left corner

    reve_girl_tl = (880 * SCALING, 1795 * SCALING) # top left corner

    final_img = Image.new('RGBA', (2000 * SCALING, 2000 * SCALING))

    unmasked_img = Image.new('RGBA', (2000 * SCALING, 2000 * SCALING))
    unmasked_img.paste(img, tl)
    unmasked_img.paste(reve_girl_img, reve_girl_tl)

    reve_img = Image.new('RGBA', (2000 * SCALING, 2000 * SCALING))
    reve_img.paste(img, tl)

    final_img = Image.composite(final_img, unmasked_img, mask)
    final_img.save("red_velvet_overlay.png")

