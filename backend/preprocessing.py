import numpy as np
from PIL import Image


def preprocess_image(source):
    """source: a file path or a file-like object (e.g. io.BytesIO)."""
    image = Image.open(source)
    image = image.convert("L")
    image = image.resize((28, 28))
    array = np.array(image).astype("float32") / 255.0
    return array.reshape(1, 28, 28, 1)