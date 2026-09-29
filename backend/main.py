from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    # TODO: preprocess `contents` and run through the trained model
    return {"label": "placeholder", "confidence": 0.0}

