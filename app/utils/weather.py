import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(lat, lng):
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    weather = {
        'description': data['weather'][0]['description'],
        'temperature': data['main']['temp'],
        'wind_speed': data['wind']['speed'],
        'rain': 'rain' in data,
        'snow': 'snow' in data,
        'city': data.get('name', 'Unknown City'),
        'country': data.get('sys', {}).get('country', 'Unknown Country')
    }
    return weather
