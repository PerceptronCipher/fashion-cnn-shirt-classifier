from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image

from preprocessing import preprocess_image
from preprocessing_clean import preprocess_clean

CLASS_NAMES = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
PREFIX = {"tshirt": 0, "trouser": 1, "pullover": 2, "dress": 3, "coat": 4,
          "sandal": 5, "shirt": 6, "sneaker": 7, "bag": 8, "boot": 9}

model = tf.keras.models.load_model("fashion_mnist_cnn.keras")
Path("debug").mkdir(exist_ok=True)
files = sorted(p for p in Path("my_photos").iterdir()
               if p.suffix.lower() in {".jpg", ".jpeg", ".png"})

raw_ok = clean_ok = n = 0
for p in files:
    key = p.stem.split("_")[0].lower()
    if key not in PREFIX:
        print(f"skipping {p.name}")
        continue
    true = PREFIX[key]
    raw = int(np.argmax(model.predict(preprocess_image(p), verbose=0)[0]))
    x = preprocess_clean(p)
    probs = model.predict(x, verbose=0)[0]
    clean = int(np.argmax(probs))
    # save what the model actually sees, enlarged, so you can look at it
    Image.fromarray((x[0, :, :, 0] * 255).astype("uint8")).resize(
        (224, 224), Image.NEAREST).save(f"debug/{p.stem}.png")
    n += 1
    raw_ok += raw == true
    clean_ok += clean == true
    print(f"{p.name:18s} true={CLASS_NAMES[true]:12s} "
          f"before={CLASS_NAMES[raw]:12s} after={CLASS_NAMES[clean]:12s} ({probs.max()*100:.0f}%)")

print(f"\nBEFORE: {raw_ok}/{n} = {100*raw_ok/n:.1f}%")
print(f"AFTER:  {clean_ok}/{n} = {100*clean_ok/n:.1f}%")