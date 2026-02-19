import pandas as pd
import matplotlib.pyplot as plt
from database import get_connection

def sentiment_distribution():
    conn=get_connection()
    query="Select sentiment_label from headlines"
    df=pd.read_sql(query,conn)
    conn.close()

    count=df["sentiment_label"].value_counts()
    print("Sentiment distribution:",count)
    
    count.plot(kind="bar")
    plt.title("Sentiment Distribution of ARY News Headlines")
    plt.xlabel("Sentiment")
    plt.ylabel("No of headlines")
    plt.show()

if __name__ == "__main__":
    sentiment_distribution()