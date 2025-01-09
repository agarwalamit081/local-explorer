document.getElementById('get-suggestion').addEventListener('click', () => {
    // Get the user's location using the browser's Geolocation API
    navigator.geolocation.getCurrentPosition(async (position) => {
        const location = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

        // Fetch weather and activity suggestions from the backend
        const response = await fetch('/get_suggestion', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ location })
        });
        const data = await response.json();

        // Display weather details
        document.getElementById('city').innerText = data.weather.city;
        document.getElementById('country').innerText = data.weather.country;
        document.getElementById('temperature').innerText = data.weather.temperature;
        document.getElementById('wind-speed').innerText = data.weather.wind_speed;
        document.getElementById('rain').innerText = data.weather.rain ? 'Yes' : 'No';
        document.getElementById('snow').innerText = data.weather.snow ? 'Yes' : 'No';

        // Display current local time
        const now = new Date();
        document.getElementById('current-time').innerText = now.toLocaleString();

        // Display activity suggestions
        const activities = data.suggestion.split('\n').filter(activity => activity.trim() !== '');
        const activityElements = [
            document.getElementById('activity-1'),
            document.getElementById('activity-2'),
            document.getElementById('activity-3'),
            document.getElementById('activity-4')
        ];

        // Clear previous activity suggestions
        activityElements.forEach(element => element.innerText = '');

        // Populate activity suggestions in the grid
        activities.forEach((activity, index) => {
            if (activityElements[index]) {
                activityElements[index].innerText = activity;
            }
        });

        // Display Google Map for the first activity
        if (data.map_url) {
            document.getElementById('map').src = data.map_url;
        } else {
            document.getElementById('map').src = ''; // Clear the map if no URL is provided
        }
    }, (error) => {
        // Handle geolocation errors
        console.error('Error getting location:', error);
        alert('Unable to retrieve your location. Please enable location services and try again.');
    });
});
