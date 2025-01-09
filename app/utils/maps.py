import os
import googlemaps
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Google Maps API client
gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

def get_place_location(place_name):
    """
    Get the latitude and longitude of a place using Google Maps API.
    """
    try:
        # Search for the place using the place name
        geocode_result = gmaps.geocode(place_name)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return location
        else:
            return None
    except Exception as e:
        print(f"Error fetching location: {e}")
        return None

def get_place_details(place_name):
    try:
        places_result = gmaps.places(query=place_name)
        if places_result['results']:
            place = places_result['results'][0]
            return {
                'name': place['name'],
                'address': place['formatted_address'],
                'location': place['geometry']['location']
            }
        else:
            return None
    except Exception as e:
        print(f"Error fetching place details: {e}")
        return None

def get_embed_map_url(lat, lng):
    """
    Generate an embed URL for Google Maps based on latitude and longitude.
    """
    return f"https://www.google.com/maps/embed/v1/view?key={os.getenv('GOOGLE_MAPS_API_KEY')}&center={lat},{lng}&zoom=15"
