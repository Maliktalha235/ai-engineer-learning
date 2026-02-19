import mysql.connector

def create_database():
        
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hitec@123"
    )
    query="""Create database if not exists news_sentiment"""
    cursor=conn.cursor()
    cursor.execute(query)
    conn.close()

def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hitec@123",
        database="news_sentiment"
    )
    return conn


def create_table():
    conn=get_connection()
    query="""Create table if not exists headlines(
            id int auto_increment primary key,
            headline text,
            scraped_at datetime,
            sentiment_score float,
            sentiment_label varchar(20)  
            )
    """
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
