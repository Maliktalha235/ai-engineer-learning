import pandas as pd
import matplotlib.pyplot as plt
from database import get_connection

def visualize():
    conn=get_connection()
    df=pd.read_sql("Select sentiment_label from yt_comments",conn)
    conn.close()
    counts=df["sentiment_label"].value_counts()
    counts.plot(kind="bar")
    plt.title("Youtube Comments Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of comments")
    plt.show()

