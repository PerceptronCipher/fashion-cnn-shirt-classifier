import numpy as np
from PIL import Image, ImageOps
from rembg import remove, new_session

_session = None


def preprocess_clean(source):
    global _session
    if _session is None:
        _session = new_session("u2netp")  # small, fast model
    image = ImageOps.exif_transpose(Image.open(source)).convert("RGB")
    image.thumbnail((512, 512))
    cut = remove(image, session=_session)          # RGBA, background transparent
    alpha = np.array(cut)[:, :, 3]
    ys, xs = np.where(alpha > 128)
    if len(xs) == 0:
        raise ValueError("no foreground found")
    cut = cut.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    black = Image.new("RGBA", cut.size, (0, 0, 0, 255))
    flat = Image.alpha_composite(black, cut).convert("L")
    flat = ImageOps.autocontrast(flat)
    side = max(flat.size)                           
    square = Image.new("L", (side, side), 0)
    square.paste(flat, ((side - flat.width) // 2, (side - flat.height) // 2))
    square = square.resize((28, 28))
    return (np.array(square).astype("float32") / 255.0).reshape(1, 28, 28, 1)