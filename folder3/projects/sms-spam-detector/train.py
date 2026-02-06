import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

df=pd.read_csv("data/spam.csv", encoding="latin-1")
#only useful data
df=df[["v1","v2"]]
df.columns=["labels","text"]
# Convert all text to strings
df["text"] = df["text"].astype(str)
#converting labels to nombers
df["labels"]= df["labels"].map({"ham":0,"spam":1})

#split data
X_train,X_test,y_train,y_test= train_test_split(df["text"],df["labels"], test_size=0.25,random_state=42)

#creating pipeline:
pipeline=Pipeline([
    ("tfidf",TfidfVectorizer(stop_words="english")),
     ("model",LogisticRegression(max_iter=1000))
     ])
#train
pipeline.fit(X_train,y_train)

#Evaluate
preds=pipeline.predict(X_test)
accuracy=accuracy_score(y_test,preds)

print("Model Accuracy: ", accuracy*100)
#saving
joblib.dump(pipeline,"model/spam_pipeline.pkl")
print("Pipeline saved successfully")
