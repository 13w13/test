import requests
import pandas as pd
import datetime

# OpenWeatherMap API endpoint
url = "https://api.openweathermap.org/data/2.5/weather"
# Coordinates for Budapest, Hungary
lat = 47.497912
lon = 19.040235
# Your API key from OpenWeatherMap
api_key = "155fc33266502758a3b3dabbe9ee8df1"

# Request data from the API
response = requests.get(url, params={"lat": lat, "lon": lon, "appid": api_key})

# Parse the JSON response
data = response.json()

# Create a pandas DataFrame from the weather data
df = pd.DataFrame({
    "temperature": [data["main"]["temp"]],
    "humidity": [data["main"]["humidity"]],
    "wind_speed": [data["wind"]["speed"]],
    "wind_direction": [data["wind"]["deg"]],
    "description": [data["weather"][0]["description"]]
})


# Add a new column with the current timestamp
timestamp = datetime.datetime.now()
df["last_approved_time"] = timestamp

# Write the DataFrame to an Excel file
filename = 'weather_forecast.xlsx'
df.to_excel(filename, index=False)

