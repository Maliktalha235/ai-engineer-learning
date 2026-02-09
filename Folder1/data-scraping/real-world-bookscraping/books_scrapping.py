import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url="https://books.toscrape.com/catalogue/"
page=1
book=[]

while page<=50:
    print(f"Scraping data from page:{page}")
    url=f"https://books.toscrape.com/catalogue/page-{page}.html"
    response= requests.get(url).text
    soup=BeautifulSoup(response,"html.parser")
    details=soup.find_all("article",class_="product_pod")
    if not details:
        break
    for data in details:
        title=data.h3.a["title"]
        price=data.find("p",class_="price_color").text.replace("£","").replace("Ã","")
        availability=data.find("p",class_="instock availability").text.strip()
        rating_class=data.find("p",class_="star-rating")["class"]
        rating=rating_class[1]
        book.append({
            "title":title,
            "price":price,
            "rating":rating,
            "availability":availability
        })
    page+=1
df=pd.DataFrame(book)
df.to_csv("Book_Data_multipages.csv",index=False)
print("Scraping complete \nTotal books:",len(df))
