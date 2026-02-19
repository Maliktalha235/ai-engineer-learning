import pandas as pd
from database import get_connection
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer=SentimentIntensityAnalyzer()

def analyze_and_update():
    conn=get_connection()
    query="select id,headline from headlines where sentiment_score is null "
    df=pd.read_sql(query,conn)
    if df.empty:
        print("No new headline to analyze")
        return
    print(f"Analyzing {len(df)} headlines...")

    def get_sentiment(text):
        score=analyzer.polarity_scores(text)["compound"]

        if score >0.05:
            label="Positive"
        elif score < 0.05:
            label="Negative"
        else: 
            label="Neutral"
        return score,label
    
    df[["sentiment_score", "sentiment_label"]]=df["headline"].apply(lambda x: pd.Series(get_sentiment(x)))
    cursor=conn.cursor()

    for _,row in df.iterrows():
        update_query="""
        update headlines set sentiment_score=%s,
        sentiment_label=%s where id=%s
        """
        cursor.execute(
            update_query,(row["sentiment_score"],
                          row["sentiment_label"],
                          row["id"])
        )
    conn.commit()
    cursor.close()
    conn.close()

    print("Sentiment analysis completed and database updated.")

if __name__ == "__main__":
    analyze_and_update()