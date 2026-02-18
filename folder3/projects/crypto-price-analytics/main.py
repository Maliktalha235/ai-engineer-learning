from scrape import create_database
from scrape import create_table
from scrape import insert_data
from scrape import fetch_prices
from datetime import datetime
import time

def main():
    create_database()
    create_table()
    print("Crypto price tracker started...")

    while True:
        try:
            data=fetch_prices()
            insert_data(data)
            print(f"inserted at {datetime.now()}→{data}")
        except Exception as e:
            print("Error:", e)

        time.sleep(60)

if __name__=="__main__":
    main()