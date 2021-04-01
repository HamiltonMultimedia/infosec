#!/usr/local/bin/python3

# import requests
from pprint import pprint

"""
Uncomment lines 3, 14, 18, 20 & 22.
If you don't already have Requests installed.
Be sure to run (python -m pip install requests) in your terminal.

Also you will need an API key from (https://openweathermap.org/guide).
"""

# API_Key = 'enter_api_key_here'

city = input("Enter a city: ")

# base_url = "http://api.openweathermap.org/data/2.5/weather?appid"+API_Key+"&q"+city

# weather_data = requests.get(base_url).json()

# pprint(weather_data)