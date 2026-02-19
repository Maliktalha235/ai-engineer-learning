from scrape import get_headlines, insert_headlines
from database import create_database, create_table
from sentiment_analysis import analyze_and_update
from analytics import sentiment_distribution

def run_pipeline():
    print("Creating database and table...")
    create_database()
    create_table()

    print("Scraping headlines...")
    data = get_headlines()
    print(f"Found {len(data)} headlines")

    print("Inserting headlines...")
    insert_headlines(data)

    print("Running sentiment analysis...")
    analyze_and_update()

    print("Generating analytics...")
    sentiment_distribution()

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
