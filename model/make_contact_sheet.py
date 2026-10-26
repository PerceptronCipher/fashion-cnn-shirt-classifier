import numpy as np
import tensorflow as tf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from preprocessing_clean import preprocess_clean

(_, _), (X, y) = tf.keras.datasets.fashion_mnist.load_data()
CLASS = {"sandal": 5, "pullover": 2, "shirt": 6, "sneaker": 7}
mine = ["sandal_01", "sandal_02", "pullover_02", "shirt_02", "sneaker_02"]

fig, axes = plt.subplots(2, len(mine), figsize=(2.2 * len(mine), 5))
for i, name in enumerate(mine):
    label = name.split("_")[0]
    idx = np.where(y == CLASS[label])[0][i]
    axes[0, i].imshow(X[idx], cmap="gray")
    axes[0, i].set_title(f"dataset: {label}", fontsize=8)
    axes[1, i].imshow(preprocess_clean(f"my_photos/{name}.jpg")[0, :, :, 0], cmap="gray")
    axes[1, i].set_title(f"mine: {name}", fontsize=8)
for a in axes.ravel():
    a.axis("off")
plt.tight_layout()
plt.savefig("debug/comparison.png", dpi=150)
print("saved debug/comparison.png")