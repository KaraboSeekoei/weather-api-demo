# Weather API Demo

**A simple CLI-based Python project demonstrating API usage and web services.**  

This project is part of my journey learning how APIs work in real-world applications. It fetches real-time weather data using the public **Open-Meteo API** and displays it in the terminal.

---

## Features

- Fetch current weather (temperature and wind speed) for selected cities
- Command-line interface (CLI) for easy interaction
- Demonstrates:
  - Making API calls
  - Using API endpoints
  - Parsing JSON responses in Python

---

## How it works

1. User enters a city name in the terminal.
2. The program looks up coordinates for that city.
3. Sends an **API call** (GET request) to the Open-Meteo **endpoint**.
4. The **web service** returns current weather data.
5. Program displays the results in a readable format.

---

## Supported Cities (for now)

- Johannesburg
- Cape Town
- Durban

---

## Requirements

- Python 3.x
- `requests` library

Install dependencies with:

```bash
pip install -r requirements.txt
````

---

## Run the Application

Run the CLI program:

```bash
python weather_app.py
```

Example interaction:

```
Enter a city (Johannesburg, Cape Town, Durban): johannesburg
Fetching current weather in Johannesburg...
Temperature: 26°C, Wind speed: 15 km/h
```