import random
import string

from PIL import Image, ImageDraw, ImageFilter, ImageFont


def generate_captcha(captcha_text, height=100, font_size=40):
    """
    Generates a CAPTCHA image with the given text and dimensions.

    Args:
        captcha_text (str): The text to be displayed in the CAPTCHA.
        height (int, optional): The height of the CAPTCHA image. Defaults to 100.
        font_size (int, optional): Font size for the CAPTCHA text. Defaults to 40.

    Returns:
        None
    """

    width = len(captcha_text) * (font_size + 10)
    image = Image.new("RGB", (width, height), color=(255, 255, 255))
    font = ImageFont.truetype("arial.ttf", font_size) or ImageFont.load_default()

    for i, char in enumerate(captcha_text):
        char_image = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
        draw = ImageDraw.Draw(char_image)
        draw.text((10, 10), char, (0, 0, 0), font=font)
        char_image = char_image.rotate(random.randint(-30, 30), expand=1)

        x = i * (font_size + 10) + 10
        y = (height - font_size) // 2

        distorted_image = apply_distortion(char_image)
        image.paste(distorted_image, (x, y), distorted_image)

    image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
    image.show()
    image.save("captcha.png")


def apply_distortion(char_image):
    """
    Applies distortion to the input character image.

    Args:
        char_image (PIL.Image.Image): The input character image to distort.

    Returns:
        PIL.Image.Image: The distorted image after applying the distortion.
    """

    width, height = char_image.size
    shifts = [random.choice([-2, -1, 1, 2]) for _ in range(width * height)]
    distorted_image = Image.new("RGBA", (width, height))

    for x in range(width):
        for y in range(height):
            index = y * width + x
            src_x = x + shifts[index]
            src_y = y + shifts[index]
            if 0 <= src_x < width and 0 <= src_y < height:
                distorted_image.putpixel((x, y), char_image.getpixel((src_x, src_y)))
    return distorted_image


def random_text(length=6):
    """
    Generates random text of a specified length using uppercase letters and digits.

    Args:
        length (int, optional): The length of the random text to generate. Defaults to 6.

    Returns:
        str: The randomly generated text.
    """

    letters = string.ascii_uppercase + string.digits
    return "".join(random.choice(letters) for _ in range(length))
