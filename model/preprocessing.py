import numpy as np
from PIL import Image
from PIL import ImageOps 

def preprocess_image(path):
    image = Image.open(path)               
    image = image.convert("L")
    image = image.convert("L")
    # image = ImageOps.invert(image)                            
    image = image.resize((28, 28))                        
    array = np.array(image).astype("float32") / 255.0 
    array = array.reshape(1, 28, 28, 1)                   
    return array

if __name__ == "__main__":
    result = preprocess_image("bag.jpg")
    print(result.shape, result.min(), result.max())