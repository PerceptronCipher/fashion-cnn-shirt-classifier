import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical

# Load the saved model
model = tf.keras.models.load_model('fashion_mnist_cnn.keras')

# Load Fashion Mnist Dataset to fetch the test data
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

# Normalize pixel values
X_test = X_test.astype('float32') / 255.0

# Reshape the images to add a channel dimension
X_test = X_test.reshape(-1, 28, 28, 1)

# One-hot encode the labels
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_accuracy*100:.2f}%")

# Make predictions on the test set
image = X_test[0:1]
predictions = model.predict(image)
print(predictions.shape)
print(f"Predicted class probabilities: {predictions}")
predicted_class = np.argmax(predictions)
print(f"Predicted class: {predicted_class}")

# Turn the numeric to names 
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(class_names[predicted_class])

# Get the class number for first image in the test set
true_class = np.argmax(y_test[0])
print(f"True class: {true_class}")
print(class_names[true_class])