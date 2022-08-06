from sys import argv, exit
from PIL import Image, ImageOps
import os

if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")

ext1 = os.path.splitext(argv[1])
ext2 = os.path.splitext(argv[2])

if ext1[-1] not in [".jpg", ".jpeg", ".png"]:
    exit("Invalid Input")

if ext1[-1] != ext2[-1]:
    exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    with Image.open(argv[1], "r") as image:
        size = shirt.size
        muppet = ImageOps.fit(image, size, bleed=0.0, centering=(0.5, 0.5))
        muppet.paste(shirt, shirt)
        muppet.save(argv[2])

except FileNotFoundError:
    exit("File does not exist")
