import io
import os

import aiofiles
from PIL import Image, ImageFilter
import aiohttp

from mini_eiko.settings import MEDIA_PATH


class BlurProcessor:
    def __init__(self):
        pass

    async def process(self, url):
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            buffer = await response.read()

        im = Image.open(io.BytesIO(buffer))

        im = im.filter(ImageFilter.GaussianBlur(radius=5))

        image_name = 'image.png'
        im.save(os.path.join(MEDIA_PATH, image_name))

        return image_name
