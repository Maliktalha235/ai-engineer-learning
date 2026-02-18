import mysql.connector

def create_database():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="123"
    )
    query="""
        create database if not exists weather_db
        """
    cursor=conn.cursor()
    cursor.execute(query)
    print("Database is created....")
    conn.close()

def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="weather_db"
    )
    return conn

def create_table():
    conn=get_connection()
    cursor=conn.cursor()
    query="""
        create table if not exists weather_data(
        id int auto_increment primary key,
        city varchar(100),
        temperature float,
        humidity int,
        weather_desc varchar(255),
        recorded_at datetime
        )
        """
    cursor.execute(query)
    print("Table created.....")

    conn.close()    
