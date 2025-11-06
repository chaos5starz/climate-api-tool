import requests
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("API-KEY")

while True :

    print("enter a city name or type exit to exit")
    city_name = input().lower()

    if city_name == "exit" :
        print("bye")
        break

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city_name,     
        "appid": api_key,   
        "units": "metric"   
    }

    headers = {
        "Content-Type": "application/json",
    }

    try :
        response = requests.get(url , headers = headers , params=params , timeout = 5)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError :
        print("invalid city name")
        continue

    except requests.exceptions.Timeout :
        print("poor connection , try again later")
        continue

    if data.get("cod") == 200 :
        print("Temp:", data["main"]["temp"])
        print("Feels like:", data["main"]["feels_like"])
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"])
        print("Wind speed:", data["wind"]["speed"])
    else :
        print ("invalid city name")
        continue