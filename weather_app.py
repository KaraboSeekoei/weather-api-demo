# --------------------------------------------
# weather_app.py
# --------------------------------------------
# This is a simple CLI-based weather app demonstrating how to use APIs.
# It fetches current weather for a few cities using the Open-Meteo API.
# Concepts demonstrated:
# - API calls
# - API endpoint
# - Web service
# - Query parameters
# - JSON response parsing
# - Using a Python dictionary for API parameters
# --------------------------------------------

import requests  # Library for making HTTP requests (API calls)

# --------------------------------------------
# Dictionary of cities and their coordinates
# --------------------------------------------
# Each city maps to a tuple of (latitude, longitude)
# The API needs coordinates, not city names, to return weather data
cities = {
    "johannesburg": (-26.2041, 28.0473),
    "cape town": (-33.9249, 18.4241),
    "durban": (-29.8587, 31.0218)
}

# --------------------------------------------
def get_weather(latitude, longitude):
    """
    Fetch current weather for given coordinates using the Open-Meteo API.
    
    Key concepts:
    - API Endpoint: URL of the web service ("https://api.open-meteo.com/v1/forecast")
    - API Call: requests.get(api_url, params=params) sends our request
    - Parameters: Tell the API what data we want (latitude, longitude, current_weather)
    - Web Service: The API server receives the request, finds the data, and returns it
    - JSON Response: response.json() converts the API's JSON reply into a Python dictionary
    """

    # The API endpoint (the "doorway" to the web service)
    api_url = "https://api.open-meteo.com/v1/forecast"

    # Parameters sent to the API
    params = {
        "latitude": latitude,        # Required: how far north/south
        "longitude": longitude,      # Required: how far east/west
        "current_weather": True      # Optional: include current weather now
    }

    # --------------------------
    # Make the API call (HTTP GET)
    # --------------------------
    # requests automatically converts the dictionary into a URL query string
    # Example URL sent:
    # https://api.open-meteo.com/v1/forecast?latitude=-26.2041&longitude=28.0473&current_weather=True
    response = requests.get(api_url, params=params)

    # --------------------------
    # Check if the request succeeded
    # --------------------------
    if response.status_code == 200:
        # Convert the JSON response into a Python dictionary
        data = response.json()

        # Extract the 'current_weather' section from the JSON
        weather = data.get("current_weather", {})

        # Extract temperature and wind speed from the API response
        temp = weather.get("temperature")
        wind = weather.get("windspeed")

        # Return a formatted string for the CLI
        return f"Temperature: {temp}°C, Wind speed: {wind} km/h"

    else:
        # If the request failed, return the HTTP status code
        return f"Failed to get weather data. Status code: {response.status_code}"


# --------------------------------------------
# Main program (CLI)
# --------------------------------------------
if __name__ == "__main__":
    # Ask the user for a city name
    # .strip() removes extra spaces, .lower() ensures it matches our dictionary keys
    city_input = input("Enter a city (Johannesburg, Cape Town, Durban): ").strip().lower()

    # Check if the city is in our dictionary
    if city_input in cities:
        # Get the coordinates
        latitude, longitude = cities[city_input]

        # Inform the user that we are fetching the weather
        print(f"Fetching current weather in {city_input.title()}...")

        # Call the API function
        result = get_weather(latitude, longitude)

        # Display the weather info
        print(result)
    else:
        # City not recognized
        print("Sorry, that city is not in our list.")