import io
from pathlib import Path

import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import UnidentifiedImageError

from preprocessing_clean import preprocess_clean

CLASS_NAMES = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# Loaded once at startup, not per request
MODEL_PATH = Path(__file__).parent / "fashion_mnist_cnn.keras"
model = tf.keras.models.load_model(MODEL_PATH)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def warm_up():
    # Loads the background-removal model now, so the first real request isn't slow
    try:
        blank = io.BytesIO()
        from PIL import Image
        Image.new("RGB", (64, 64), (200, 200, 200)).save(blank, format="JPEG")
        blank.seek(0)
        preprocess_clean(blank)
    except ValueError:
        pass  # a blank image has no foreground; the model is loaded either way


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        batch = preprocess_clean(io.BytesIO(contents))
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="File is not a valid image")
    except ValueError:
        raise HTTPException(status_code=422, detail="Could not find an item in the photo")

    probs = model.predict(batch, verbose=0)[0]
    top3 = np.argsort(probs)[::-1][:3]
    predictions = [
        {"label": CLASS_NAMES[i], "confidence": float(probs[i])} for i in top3
    ]
    return {
        "label": predictions[0]["label"],
        "confidence": predictions[0]["confidence"],
        "top3": predictions,
    }