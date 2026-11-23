import math
import random
from cmath import rect

import PIL.Image

class QrGen:
    def __init__(self):
        pass

    @staticmethod
    def qr_gen(total_size = 16):
        pixels = []
        for i in range(total_size):
            pixels.append(random.randint(0,1))

        return pixels

    @staticmethod
    def get_pixel_square_size(pixels):
        pixels_count = len(pixels)
        return QrGen.get_square_size(pixels_count)

    @staticmethod
    def get_square_size(size):
        rect = [int(math.sqrt(size)), int(math.sqrt(size))]

        if rect[0] * rect[1] != size:
            return None

        return rect

    @staticmethod
    def make_image(pixels, width, height):
        image = PIL.Image.new("1", (width, height))

        for y in range(height):
            for x in range(width):
                image.putpixel((x, y), pixels[y * width + x])

        return image