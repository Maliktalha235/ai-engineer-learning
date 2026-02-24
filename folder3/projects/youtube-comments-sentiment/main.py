from scraper import fetch_comments
from database import create_database, create_table, insert_comments
from youtube_sentiment import analyze_comments
from analytics import visualize

def run_pipeline():
    # scraping
    comments = fetch_comments()

    # DB setup
    create_database()
    create_table()

    print("Inserting into database:")
    insert_comments(comments)

    #Sentiment analysis
    analyze_comments()

    visualize()

if __name__ == "__main__":
    run_pipeline()