# local-explorer
local-explorer

An application "Local Explorer" that instantly knows where you are, understands the weather, and suggests the perfect activity for the given moment.

Core Functionalities:
1. Geolocation and Weather Data Integration:
Utilizes browser-based geolocation to identify the user's current location and integrate a weather API to access real-time weather data for that location.

2. AI-Driven Activity Suggestions:
Uses OpenAI GPT-3 to generate activity suggestions that are relevant to the local weather conditions and time and ensures that the activities are varied and include both outdoor and indoor options.

3. Google Maps Integration:
Uses Google Maps API to display the location of suggested activities, considering factors such as opening hours to ensure the suggestions are viable.

4. Unique and Dynamic Suggestions:
The app dynamically updates recommendations based on user interactions.

To run the app:
docker-compose build
docker-compose up

 Navigate to
 http://localhost:5000/
 
