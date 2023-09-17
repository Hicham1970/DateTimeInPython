from PIL import Image, ImageFilter, ImageEnhance
import os


path = "./img"
pathOut = "/edited_img"

for photo in os.listdir(path):
    img = Image.open(f"{path}/{photo}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(0)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(photo)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
