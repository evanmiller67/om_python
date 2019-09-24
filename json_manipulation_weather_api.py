#/usr/bin/env python3
"""
title: json_manipulation_weather_api.py
author: exm5840
date(created): 2019-09-19 17:57:05 EDT
date (updated): 2019-09-19 17:57:05 EDT
"""
import json
import requests


API_KEY='c3d53e77cd62c7674fbf566c9ebbed11'
command = f"http://api.openweathermap.org/data/2.5/weather?q=Austin,us&units=imperial&APPID={API_KEY}"
print(command)
response = requests.get(command)
print(json.dumps(response.json(), indent=4))
austin_data = response.json()
print(austin_data['main'])
## >>> {'temp': 84.18, 'pressure': 1019, 'humidity': 70, 'temp_min': 80.6, 'temp_max': 87.8}
print(f"""Temperature: {austin_data['main']['temp']} F
Humidity: {austin_data['main']['humidity']}%""")
