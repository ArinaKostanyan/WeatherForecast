import os
import requests

from typing import Dict
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('WEATHER_API_KEY')

# api_key= '9971cbdd16234d21a21153804251901' # Set up your API key:

def get_info(location, temp_type='celsius') -> Dict:
    url = f'https://api.weatherapi.com/v1/current.json?q={location}&key={api_key}'
    weather = {}
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()  

        if response.status_code != 200:
            print(f"Error: {data.get('error', {}).get('message', 'Unknown error')}")
            return
        
        current = data['current']
        weather['temperature'] = current['temp_c'] if temp_type.lower() == 'celsius' else current['temp_f']
        weather['description'] = current['condition']['text']
        weather['wind_speed_kmh'] = current['wind_kph']
        weather['humidity'] = current['humidity']
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the weather data: {e}")
    return weather

def get_weather_table(location):
    temp_type = input('Please, choose temperature unit (Celsius or Fahrenheit): ').strip().lower()
    
    if temp_type not in ['celsius', 'fahrenheit']:
        print("Nothing inputed. Defaulting to Celsius.")
        temp_type = 'celsius'
    
    weather_dict = get_info(location, temp_type)
    if weather_dict:
        print_weather(weather_dict, location, temp_type)

def print_weather(weather, location, temp_type):
    print("\n" + "="*30)
    print(f"Weather for {location.title()}:")
    print("="*30)
    print(f"Temperature: {weather['temperature']}°{'C' if temp_type == 'celsius' else 'F'}")
    print(f"Description: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed_kmh']} km/h")
    print("="*30 + "\n")



