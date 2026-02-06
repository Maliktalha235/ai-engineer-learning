from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

# Load pipeline
pipeline = joblib.load("model/spam_pipeline.pkl")

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model to read JSON body
class SMSInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "SMS Spam Detector is running"}

@app.post("/predict")
def predict_sms(sms: SMSInput):
    prediction = pipeline.predict([sms.text])[0]
    probability = pipeline.predict_proba([sms.text])[0]

    return {
        "prediction": "SPAM" if prediction == 1 else "NOT SPAM",
        "confidence": round(max(probability), 2)
    }
