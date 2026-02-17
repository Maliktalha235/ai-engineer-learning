import mysql.connector

def get_connection():
    conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Hitec@123",
            database="realtime_store"
    )
    if conn.is_connected():
        print("Connnection established...")
    return conn