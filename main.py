import requests
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("API-KEY")
print("enter a city name")
city_name = input()


url = "https://api.openweathermap.org/data/2.5/weather"


params = {
    "q": city_name,     
    "appid": api_key,   
    "units": "metric"   
}

headers = {
    "Content-Type": "application/json", 
}
response = requests.get(url, headers=headers , params=params)

data = response.json()

print(data)