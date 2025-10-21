import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input_image output_image")

input_path = sys.argv[1]
output_path = sys.argv[2]

def valid_extension(filename):
    return filename.lower().endswith((".jpg", ".jpeg", ".png"))

if not valid_extension(input_path) or not valid_extension(output_path):
    sys.exit("Input and output must be .jpg, .jpeg, or .png")

if os.path.splitext(input_path)[1].lower() != os.path.splitext(output_path)[1].lower():
    sys.exit("Input and output must have the same file extension")

if not os.path.exists(input_path):
    sys.exit("Input file does not exist")

input_image = Image.open(input_path)
shirt_image = Image.open("shirt.png")
input_image = ImageOps.fit(input_image, shirt_image.size)
input_image.paste(shirt_image, (0, 0), shirt_image)
input_image.save(output_path)
