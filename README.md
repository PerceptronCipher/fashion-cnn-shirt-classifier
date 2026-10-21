# Fashion MNIST Shirt Classifier: what a 90% model does on real photos

Built by **Adeyemi Ibrahim Boluwatife** (PerceptronCipher / DataCypher), AI engineer.

I trained a CNN that scores about 90% on Fashion MNIST, then pointed a phone camera at real clothes to see whether that number means anything outside the dataset. This repo is the model, the API, and the camera app used to test it.

## What I found

The benchmark images are small, centred, light-on-black clothing. Real photos are none of those. On my first real test (a mannequin in a dark jacket on a dark background):

| Preprocessing | Top 3 predictions |
|---|---|
| Grayscale, resize to 28x28 | Shirt 64.8%, T-shirt/top 34.7%, Pullover 0.4% |
| Same, with colours inverted | Bag 46.2%, T-shirt/top 21.8%, Shirt 17.4% |

Inverting the image, which fixes light backgrounds, turned a decent answer into a wrong one. The right preprocessing depends on the photo, and the model can't tell you that. This is one photo, and I'm building a larger set of my own to measure it properly.

## What's in it

- `model/`: the CNN (3 conv layers, about 90.4% test accuracy), training script and preprocessing
- `backend/`: FastAPI service with one endpoint, `POST /predict`, that returns the top 3 classes
- `frontend/`: Next.js camera app that sends a photo to the API and shows the result

## Run it

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload

cd ../frontend
echo "NEXT_PUBLIC_API_URL=http://127.0.0.1:8000" > .env.local
npm install && npm run dev
```

Open `http://localhost:3000`. The camera only works on localhost or HTTPS.

## Next

Photo upload, automatic background detection, a test set of my own photos with before/after accuracy, and a public deployment.

## Author

Adeyemi Ibrahim Boluwatife
[GitHub](https://github.com/PerceptronCipher) | [LinkedIn](https://www.linkedin.com/in/adeyemi-ibrahim-boluwatife-74329a383)

MIT License