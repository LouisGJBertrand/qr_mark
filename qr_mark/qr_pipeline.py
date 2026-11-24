import os

from qr_mark.qr_gen import QrGen
from qr_mark.qr_settings import QrSettings

class QrPipeline:
    def __init__(self, settings=QrSettings()):
        self.settings = settings

    def generate_images(self):
        images = []

        for i in range(self.settings.count):
            pixels = QrGen.qr_gen(self.settings.size)
            rect = self.settings.get_size_rect()

            if rect is None:
                raise Exception("invalid size, can't calculate image size")

            image = QrGen.make_image(pixels, rect[0], rect[1])

            images.append(image)

        return images

    def save_images(self, images):
        self.make_dirs()
        i = 0
        for image in images:
            image.save(self.settings.get_output(i))
            i+=1

    def make_dirs(self):
        os.makedirs(os.path.dirname(self.settings.output), exist_ok=True)