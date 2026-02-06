# SMS Spam Detector
A machine learning basic web application that detects whether an SMS message is spam or not.
## Features
The model is trained using an end-to-end **ML pipeline** that includes:
- Text vectorization (TF-IDF)
- Classification model
- Saved pipeline for reuse in real-world applications
The complete pipeline is saved using `joblib` and stored inside the `model/` directory.

## Tech Stack
- Python
- Scikit-learn
- FastAPI
- HTML

## How to Run
1. Install dependencies
2. Run: `uvicorn app:app --reload`
3. Open browser at `http://127.0.0.1:8000`
