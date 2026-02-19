import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database import create_database,get_connection,create_table

url="https://live.arynews.tv/"

def get_headlines():
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    headlines=[]
    for item in soup.find_all("h5"):
        text=item.get_text(strip=True)
        if text:
            headlines.append({
                "headline":text,
                "scraped_at": datetime.now()
             })
    return headlines

def insert_headlines(data):
        conn=get_connection()
        cursor=conn.cursor()
        query="insert into headlines(headline, scraped_at) values(%s,%s)"
        for item in data:
             cursor.execute(query,(item["headline"],item["scraped_at"]))
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == "__main__":
    data = get_headlines()
    print(f"Found {len(data)} headlines")
    print("Sample headlines:", data[:5])

    print("Creating database...")
    create_database()
    print( "creating table headlines....")
    create_table()
    print("Inserting data to database...")
    insert_headlines(data)

   