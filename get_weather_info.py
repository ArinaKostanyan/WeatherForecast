import requests
import pandas as pd

from typing import Dict


api_key= '9971cbdd16234d21a21153804251901'

def get_info(location, temp_type = 'celsius')->Dict:
    url = f'https://api.weatherapi.com/v1/current.json?q={location}&key={api_key}'
    response  = requests.get(url)

    weather = {}

    if response.status_code == 200:
        r_t = eval(response.text)['current']
        weather['temperature'] = r_t['temp_c'] if temp_type.lower() == 'celsius' else r_t['temp_f']
        weather['description'] = r_t['condition']['text']
        weather['wind_speed_kmh'] = r_t['wind_kph']
        weather['humidity'] = r_t['humidity']
    return weather

def get_weather_table(location, temp_type):
    weather_info = pd.DataFrame(get_info(location, temp_type))
    print(weather_info)