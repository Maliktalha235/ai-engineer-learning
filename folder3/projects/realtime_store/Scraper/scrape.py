from bs4 import BeautifulSoup
import requests
import time
base_url="https://webscraper.io/test-sites/e-commerce/static/computers"

def scrape_category(category):
    page=1
    all_products=[]

    while True:

        url = f"{base_url}/{category}?page={page}"
        print(f"Scraping {url}")

        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to fetch page")
            break
        
        soup=BeautifulSoup(response.text, "html.parser")
        products=[]
        items= soup.find_all("div", class_="thumbnail")
        if not items:
            print("No iems found..")
            break
        else:
            print(f"Found {len(items)} products")

        for item in items:
            title=item.find("a",class_="title").text.strip()
            price=float(item.find("h4",class_="price").text.strip().replace("$",""))
            description=item.find("p",class_="description").text.strip()
            rating_div=item.find("div",class_="ratings")
            if rating_div:
                rating = len(rating_div.find_all("span", class_="ws-icon-star"))
            else:
                rating = 0

            all_products.append({
                "title": title,
                "price":price,
                "description": description,
                "category": category,
                "rating":rating 
            })
        page+=1
        time.sleep(1)
    print(f"Total scraped in {category}: {len(all_products)}")
    return all_products
 
def scrape_all_categories():
    categories=["laptops","tablets"]
    all_data=[]
    for category in categories:
        data=scrape_category(category)
        all_data.extend(data)
    
    print(f"Grand total scraped: {len(all_data)}")
    return all_data