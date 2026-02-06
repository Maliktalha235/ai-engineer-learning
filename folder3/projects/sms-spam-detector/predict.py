import joblib
pipeline=joblib.load("model/spam_pipeline.pkl")
print("SMS Spam Detector ('Type exit to quit')")
while True:
    text=input("Enter your text: ")
    if text.lower()=='exit':
        break
    prediction=pipeline.predict([text])[0]
    probability= pipeline.predict_proba([text])[0]

    print("Prediction:", "Spam" if prediction==1 else "Not Spam")
    print("Confidence: ", round(max(probability),2))
