# **Local Explorer**

An application that instantly knows where you are, understands the weather, and suggests the perfect activity for the given moment.

---

## **Core Functionalities**

1. **Geolocation and Weather Data Integration**:
   - Utilizes browser-based geolocation to identify the user's current location.
   - Integrates a weather API to access real-time weather data for that location.

2. **AI-Driven Activity Suggestions**:
   - Uses OpenAI's GPT-3 to generate activity suggestions that are relevant to the local weather conditions and time.
   - Ensures that the activities are varied and include both outdoor and indoor options.

3. **Google Maps Integration**:
   - Uses Google Maps API to display the location of suggested activities.
   - Considers factors such as opening hours to ensure the suggestions are viable.

4. **Unique and Dynamic Suggestions**:
   - The app dynamically updates recommendations based on user interactions.

---

## **How to Use the Application**

1. **Enable the API Keys**:
   - Add the following keys to the `.env` file:
     ```
     OPENWEATHERMAP_API_KEY="Enter your key here"
     GOOGLE_MAPS_API_KEY="Enter your key here"
     GPT3_API_KEY="Enter your key here"
     ```

2. **Build and Run the Application**:
   - Build the Docker image:
     ```bash
     docker-compose build
     ```
   - Start the Docker container:
     ```bash
     docker-compose up
     ```

3. **Access the Application**:
   - Navigate to:
     ```
     http://localhost:5000/
     ```
   - Ensure that your browser has permission to access your location.

---

## **Requirements**

- Docker and Docker Compose installed.
- Valid API keys for OpenWeatherMap, Google Maps, and OpenAI GPT-3.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## **Contact**

For questions or feedback, please contact [Your Name](mailto:agarwalamit081@gmail.com).
