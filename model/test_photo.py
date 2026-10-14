import numpy as np
import tensorflow as tf
from preprocessing import preprocess_image

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

model = tf.keras.models.load_model("fashion_mnist_cnn.keras")

image = preprocess_image("shirt.jpg")
probs = model.predict(image)[0]

top3 = np.argsort(probs)[::-1][:3]
for i in top3:
    print(f"{class_names[i]}: {probs[i]*100:.1f}%")