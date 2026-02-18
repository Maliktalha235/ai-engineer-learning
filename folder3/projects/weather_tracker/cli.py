from scraper import fetch_data
from database.db import create_database,create_table
from database.insert import insert_weather

def main():
    print("Weather Data Tracker\n")
    create_database()
    create_table()
    while True:
        city = input("Enter city (or type exit): ")

        if city.lower() == "exit":
            break

        weather = fetch_data(city)

        if weather:
            insert_weather(weather)
        else:
            print("City not found or API error.")

if __name__ == "__main__":
    main()
