# import requests

# url="https://api.coingecko.com/api/v3/simple/price"
# params= {

#     "ids":"bitcoin, ethereum",
#     "vs_currencies":"usd"
# }
# response=requests.get(url,params=params)
# data=response.json()
# print(data)

import requests
import time
import mysql.connector
from datetime import datetime 

def create_database():

    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hitec@123"
        )
    query="Create database if not exists crypto_db"
    cursor=conn.cursor()
    cursor.execute(query)
    conn.close()

def create_table():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hitec@123",
        database="crypto_db"
        )
    query="""Create table if not exists crypto_prices
            (id int auto_increment primary key,
            coin varchar(50),
            price decimal(18,8),
            currency varchar(10),
            created_at timestamp default current_timestamp 
            )
    
    """
    cursor=conn.cursor()
    cursor.execute(query)
    conn.close()

# Fetch data:
def fetch_prices():
    url="https://api.coingecko.com/api/v3/simple/price"

    params={
        "ids":"bitcoin,ethereum",
        "vs_currencies": "usd"
        }
    response=requests.get(url, params=params)
    data=response.json()
    return data
    
def insert_data(data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hitec@123",
        database="crypto_db"
    )
    cursor = conn.cursor()
    
    # Define query ONCE outside the loop
    query = "INSERT INTO crypto_prices (coin, price, currency) VALUES (%s, %s, %s)"
    
    # Loop through all coins
    for coin in data:
        price = data[coin]["usd"]
        values = (coin, price, "usd")
        cursor.execute(query, values)  # Insert current coin
        print(f"Inserted {coin}: ${price}")  # Optional: see progress
    
    # Commit once after ALL inserts
    conn.commit()
    conn.close()
