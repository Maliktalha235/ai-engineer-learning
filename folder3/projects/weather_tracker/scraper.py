import requests
from datetime import datetime

API_key="2b0f77b42ba9f73dc0df5ff265cd69e2"

def fetch_data(city):
    url="https://api.openweathermap.org/data/2.5/weather"
    params= {
        "q":city,
        "appid":API_key,
        "units":"metric"
        }
    response=requests.get(url,params=params)
    data=response.json()
    if response.status_code !=200:
        print("Error:",data.get( "message"))
        return None
    
    weather={
        "city":data["name"],
        "temperature":data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather_desc": data["weather"][0]["description"],
        "recorded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return weather