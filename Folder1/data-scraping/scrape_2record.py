import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://quotes.toscrape.com/"
html=requests.get(url).text
soup=BeautifulSoup(html,"html.parser")
records=[]
block_quote= soup.find_all("div",class_="quote")

for block in block_quote:
    texts=block.find("span",class_="text").text
    author=block.find("small",class_="author").text
    
    records.append({
        "quote":texts,
        "author": author
    })

print(records[0])

def clean_text(text):
    text = text.lower()
    text = text.strip()
    text = text.replace("“", "").replace("”", "")
    return text

cleaned_records = []

for r in records:
    cleaned_records.append({
        "quote": clean_text(r["quote"]),
        "author": clean_text(r["author"])
    })

print(cleaned_records[0])



df = pd.DataFrame(cleaned_records)
df.to_csv("quotes_with_authors.csv", index=False)

print("Dataset saved")
