# 576a96e4f13a4be5b9932052231905
import requests
import json
api_key = "yourKeyHere"
while True:
    city = str(input("Enter city name? "))
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes")

    if (response.status_code==200):
       # print(response.text) # The type will be string but we want dictionary
        data = response.json()
        print(f"City Name: \t\t{data['location']['name']}")
        print(f"Country Name: \t\t{data['location']['country']}")
        print(f"Temperature: \t\t{data['current']['temp_c']}")
        print(f"Humidity: \t\t{data['current']['humidity']}")
        print("")
