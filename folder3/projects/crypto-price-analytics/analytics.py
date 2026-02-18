import mysql.connector

def get_connection():
    conn=mysql.connector.connect(

        host="localhost",
        user="root",
        password="Hitec@123",
        database="crypto_db"
    )
    return conn

def latest_price(coin):

    conn=get_connection()
    cursor=conn.cursor()
    query="""
        select price,created_at from crypto_prices where coin=%s
        order by created_at Desc limit 1
        """
    cursor.execute(query,(coin,))
    result=cursor.fetchone()
    conn.close()
    return result

def price_stats(coin):
    conn=get_connection()
    cursor=conn.cursor()
    query="""
        select avg(price),
        max(price),
        min(price) from crypto_prices
        where coin=%s and created_at>=now()-interval 1 day
        """
    cursor.execute(query,(coin,))
    result=cursor.fetchone()
    conn.close()
    return result
