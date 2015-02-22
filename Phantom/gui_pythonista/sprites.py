# -*- coding: utf-8 -*-

"""Load images into a scene-usable image."""

import scene
import Image
import os

folder = 'imgs'
format = 'Chess set images {} {}.jpg'

files = [os.path.join(folder, format.format(color, type))
         for type in ('pawn', 'rook', 'queen', 'king', 'bishop', 'knight')
         for color in ('black', 'white')]

img_names = {}
for file in files:
    name = os.path.split(file)[1]
    im = Image.open(file).convert('RGBA')
    im.show()
    img = scene.load_pil_image(im)
    img_names.update({name: img})

if __name__ == '__main__':
    for key in img_names:
        print key, img_names[key]

