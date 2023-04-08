import random
import os
from PIL import Image, ImageFilter

input_path = input("Inserisci il percorso dell'immagine di input: ")


noise_level = float(input("Inserisci il livello di noise (da 0.2 a 10): "))
disturb_level = float(
    input("Inserisci il livello di disturbo (da 0.2 a 10): "))
dither_level = float(
    input("Inserisci il livello di dithering (da 0.2 a 10): "))


noise_level = max(min(noise_level, 10), 0.2)
disturb_level = max(min(disturb_level, 10), 0.2)
dither_level = max(min(dither_level, 10), 0.2)

with Image.open(input_path) as img:

    img = img.filter(ImageFilter.GaussianBlur(radius=noise_level))

    img = img.point(lambda p: p + int((disturb_level * 5)
                    * (random.random() - 0.5)))

    dither_scale = int((dither_level / 10) * 255)
    img = img.convert('P', dither=Image.FLOYDSTEINBERG, colors=dither_scale)

    output_path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "output.png")

    img.save(output_path)

    print("Immagine salvata in:", output_path)
