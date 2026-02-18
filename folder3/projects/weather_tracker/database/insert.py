import mysql.connector
from scraper import fetch_data
from database.db import create_database,create_table,get_connection

def insert_weather(weather):
    conn=get_connection()
    cursor=conn.cursor()
    query="""insert into weather_data(city,temperature,humidity,weather_desc,recorded_at)
            values(%s,%s,%s,%s,%s)
    """
    cursor.execute(query,(weather["city"],
                        weather["temperature"],
                        weather["humidity"],
                        weather["weather_desc"],
                        weather["recorded_at"]
                        ))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Inserted weather for {weather['city']} at {weather['recorded_at']}")