import requests
from bs4 import BeautifulSoup
import pandas as pd

all_records=[]
for page in range(1,6):
    url=f"https://quotes.toscrape.com/page/{page}/"
    html=requests.get(url).text
    soup=BeautifulSoup(html,"html.parser")
    quote_soup=soup.find_all("div",class_="quote")

    for block in quote_soup:
        quote=block.find("span",class_="text").text
        author=block.find("small",class_="author").text

        all_records.append({
            "quote":quote,
            "author":author
        })
print("Total records scrapped:", len(all_records))

def preprocess(text):
    text=text.lower()
    text=text.strip()
    text=text.replace("“","").replace("”","")
    return text

cleaned_data=[]
for data in all_records:
    cleaned_data.append({
        "quote":preprocess(data["quote"]),
        "author":preprocess(data["author"])
    })

df=pd.DataFrame(cleaned_data)
df.to_csv("Multipage_Scrapped_data.csv",index=False)
print("Dataset created....")
