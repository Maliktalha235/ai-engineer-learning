import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def create_database():
    conn=mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
        )
    query="Create database if not exists youtube_db"
    cursor=conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.close()

def get_connection():
    conn=mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conn

def create_table():
    conn=get_connection()
    query="""
        create table if not exists yt_comments(
        id int auto_increment primary key,
        comment text,
        scraped_at Datetime,
        sentiment_score float,
        sentiment_label varchar(20)
        )
        """
    cursor=conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.close()

def insert_comments(comments):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO yt_comments(comment, scraped_at)
    VALUES (%s, %s)
    """

    for comment in comments:
        cursor.execute(query, (comment, datetime.now()))

    conn.commit()
    cursor.close()
    conn.close()