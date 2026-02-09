import pandas as pd
import mysql.connector

df=pd.read_csv("Cleaned_Bookdata.csv")

#connection
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hitec@123",
    database="book_scrapping_db"

)
cursor=conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO books (title, price, rating, availability)
        VALUES (%s, %s, %s, %s)
        """,
        (
            row["title"],
            row["price"],
            row["rating"],
            row["availability"]
        )
    )

conn.commit()
cursor.close()
conn.close()

