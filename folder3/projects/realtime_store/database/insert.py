from database.db import get_connection

def insert_products(products):
    conn=get_connection()
    cursor=conn.cursor()

    query="""Insert ignore into products (title, price, description, category, rating) values(%s,%s,%s,%s,%s)"""

    for product in products:
        cursor.execute(query,(
            product["title"],
            float(product["price"],),
            product["description"],
            product["category"],
            product["rating"]
        ))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted successfully")