
import pprint

import requests

KEY = "e711a8a77a9d620de75b07041cd4efa9"


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric"
    return requests.get(url).json()


pprint.pprint(get_weather("London"))