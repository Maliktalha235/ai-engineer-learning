from database import get_connection
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from preprocess import clean_text

analyzer= SentimentIntensityAnalyzer()
def analyze_comments():
    conn=get_connection()
    query="""select id,comment from yt_comments where
            sentiment_score is NULL"""
    df=pd.read_sql(query,conn)
    if df.empty:
        print("No new comments")
        return

    def get_sentiment(text):
        cleaned=clean_text(text)
        score=analyzer.polarity_scores(cleaned)["compound"]

        if score >= 0.05:
            label="Positive"
        elif score <= -0.05:
            label="Negative"
        else:
            label="Neutral"
        return score, label

    df[["sentiment_score", "sentiment_label"]] =df["comment"].apply(lambda x:pd.Series(get_sentiment(x)))
    cursor=conn.cursor()

    for _,row in df.iterrows():
        cursor.execute("""
        update yt_comments set sentiment_score=%s, sentiment_label=%s
        where id=%s
        """,(row["sentiment_score"],row["sentiment_label"],row["id"]))
    conn.commit()
    cursor.close()
    conn.close()
    print("Sentiment updated")
