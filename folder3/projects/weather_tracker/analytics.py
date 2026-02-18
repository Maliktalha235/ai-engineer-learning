import pandas as pd
from database.db import get_connection
import mysql.connector

def load_data():
    conn=get_connection()
    df=pd.read_sql("select * from weather_data",conn)
    conn.close()
    return df

def show_stats():
    df=load_data()
    print("\n Weather Analytics")
    print("Total records: ", len(df))

    print("City groups:")
    print(df["city"].value_counts())

    print("\nTemperature Stats:")
    print(df["temperature"].describe())

    print("\nHumidity stats:")
    print(df["humidity"].describe())


show_stats()