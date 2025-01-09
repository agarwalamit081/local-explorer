from flask import Blueprint, render_template, request, jsonify
from .utils.weather import get_weather
from .utils.gpt3 import get_activity_suggestion
from .utils.maps import get_place_location, get_embed_map_url

# Create a Blueprint for the routes
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return render_template('index.html')

@main_routes.route('/get_suggestion', methods=['POST'])
def get_suggestion():
    # Get user's location from the frontend
    data = request.json
    location = data.get('location')
    lat = location['lat']
    lng = location['lng']

    # Fetch weather data
    weather = get_weather(lat, lng)

    # Get activity suggestions using GPT-3
    suggestion = get_activity_suggestion(weather)

    # Extract the first activity for Google Maps
    first_activity = suggestion.split('\n')[0].replace('1. ', '').split(' - ')[0]
    place_location = get_place_location(first_activity)

    # Generate Google Maps embed URL
    map_url = None
    if place_location:
        map_url = get_embed_map_url(place_location['lat'], place_location['lng'])

    # Return JSON response
    return jsonify({
        'weather': {
            'city': weather.get('city', 'Unknown City'),
            'country': weather.get('country', 'Unknown Country'),
            'temperature': weather.get('temperature', 'N/A'),
            'wind_speed': weather.get('wind_speed', 'N/A'),
            'rain': weather.get('rain', False),
            'snow': weather.get('snow', False)
        },
        'suggestion': suggestion,
        'map_url': map_url
    })
