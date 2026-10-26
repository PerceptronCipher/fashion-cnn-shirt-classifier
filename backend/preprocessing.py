import numpy as np
from PIL import Image, ImageOps


def preprocess_image(source):
    """source: a file path or a file-like object (e.g. io.BytesIO)."""
    image = Image.open(source)
    image = ImageOps.exif_transpose(image)  # fix phone-photo rotation
    image = image.convert("L")
    # image = ImageOps.invert(image)  # off for now
    image = image.resize((28, 28))
    array = np.array(image).astype("float32") / 255.0
    return array.reshape(1, 28, 28, 1)