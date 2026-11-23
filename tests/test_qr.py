import os

from qr_mark.qr_gen import QrGen
from qr_mark.qr_settings import QrSettings
from qr_mark.qr_pipeline import QrPipeline
from qr_mark.qr_cli import QrCLI

from os import listdir
from os.path import isfile, join

def test_qr_gen():
    pixels = QrGen.qr_gen()
    assert pixels.__len__() == 16

    pixels = QrGen.qr_gen(64)
    assert pixels.__len__() == 64

def test_qr_rect():
    pixels = QrGen.qr_gen(64)
    assert pixels.__len__() == 64
    rect = QrGen.get_pixel_square_size(pixels)

    assert rect[0] == 8
    assert rect[1] == 8

    pixels = QrGen.qr_gen(63)
    rect = QrGen.get_pixel_square_size(pixels)
    assert rect is None

    pixels = QrGen.qr_gen(9)
    assert pixels.__len__() == 9
    rect = QrGen.get_pixel_square_size(pixels)
    assert rect[0] == 3
    assert rect[1] == 3

    pixels = QrGen.qr_gen(8)
    rect = QrGen.get_pixel_square_size(pixels)
    assert rect is None

def test_qr_make_image():
    os.makedirs("tests/data", exist_ok=True)
    
    pixels = QrGen.qr_gen(64)
    rect = QrGen.get_pixel_square_size(pixels)

    image = QrGen.make_image(pixels, rect[0], rect[1])
    image.save("tests/data/generate_1.png")
    assert isfile(f"tests/data/generate_1.png")

    pixels = QrGen.qr_gen(256)
    rect = QrGen.get_pixel_square_size(pixels)

    image = QrGen.make_image(pixels, rect[0], rect[1])
    image.save("tests/data/generate_2.png")
    assert isfile(f"tests/data/generate_2.png")

    pixels = QrGen.qr_gen(9)
    rect = QrGen.get_pixel_square_size(pixels)

    image = QrGen.make_image(pixels, rect[0], rect[1])
    image.save("tests/data/generate_3.png")
    assert isfile(f"tests/data/generate_3.png")

    pixels = QrGen.qr_gen(25)
    rect = QrGen.get_pixel_square_size(pixels)

    image = QrGen.make_image(pixels, rect[0], rect[1])
    image.save("tests/data/generate_4.png")
    assert isfile(f"tests/data/generate_4.png")

    pixels = QrGen.qr_gen(16)
    rect = QrGen.get_pixel_square_size(pixels)

    image = QrGen.make_image(pixels, rect[0], rect[1])
    image.save("tests/data/generate_5.png")
    assert isfile(f"tests/data/generate_5.png")

def test_settings_format():
    settings = QrSettings()

    assert settings.get_output(3) == "./out/mark_003.png"

def test_settings_size():
    settings = QrSettings(size=25)
    assert settings.get_size_rect() == [5, 5]

    settings = QrSettings(size=50, x=5)
    assert settings.get_size_rect() == [5, 10]

    settings = QrSettings(size=50, y=5)
    assert settings.get_size_rect() == [10, 5]

    settings = QrSettings(size=42, y=6)
    assert settings.get_size_rect() == [7, 6]

    settings = QrSettings(x= 7, y= 7)
    assert settings.get_size_rect() == [7, 7]

    settings = QrSettings(x= 6, y= 7)
    assert settings.get_size_rect() == [6, 7]

def test_pipeline_gen():
    settings = QrSettings(count=8)
    pipeline = QrPipeline(settings)

    images = pipeline.generate_images()
    assert images.__len__() == 8

def test_pipeline_save():
    settings = QrSettings(count=8, output="./tests/data/batch/%03d.png")
    pipeline = QrPipeline(settings)

    images = pipeline.generate_images()
    pipeline.save_images(images)

    output_path = "./tests/data/batch/"

    expected_output_files = ["000.png", "001.png", "002.png", "003.png", "004.png", "005.png", "006.png", "007.png"]
    output_files = [f for f in listdir(output_path) if isfile(join(output_path, f))]

    expected_output_files.sort()
    output_files.sort()

    assert output_files == expected_output_files

def test_cli_args():
    expected_settings = QrSettings()
    actual_settings = QrCLI.get_settings_from_cli_args([])

    assert actual_settings.compare(expected_settings)

    expected_settings = QrSettings(count=5, output="./test", size=25, x=5, y=5)
    actual_settings = QrCLI.get_settings_from_cli_args(["-c", "5", "-o", "./test", "-s", "25", "-x", "5", "-y", "5"])

    assert actual_settings.compare(expected_settings)

    expected_settings = QrSettings(size=50, y=5)
    actual_settings = QrCLI.get_settings_from_cli_args(["-s", "50", "-y", "5"])

    assert actual_settings.compare(expected_settings)