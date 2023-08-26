import requests
import json
import os

city = input("Enter the name of the city : ")

url = f"https://api.weatherapi.com/v1/current.json?key=79f4f9c80e8b4b4d90364511232006&q={city}"

req = requests.get(url)
wdict = json.loads(req.text)
temp = wdict["current"]["temp_c"]

os.system(f"say 'The current weather in {city} is {temp} degrees centigrade'")