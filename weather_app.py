import requests
import datetime

API_KEY = "enter your API Key here"
BASE_URL = "https://api.openweathermap.org/data/2.5"

def get_weather(city):
    current_url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    response = requests.get(current_url, params = params)

    if response.status_code != 200:
        print("Error: City not found or API issue.")
        print(f"Status code: {response.status_code}")
        return None

    return response.json()

def get_forecast(city):
    forecast_url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    response = requests.get(forecast_url, params = params)
    if response.status_code == 200:
        return response.json()

    else:
        print("Could not fetch forecast.")
        return None

def display_current_weather(data):
    if not data:
        return

    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"].capitalize()
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"\n🌤️  Current Weather in {city}, {country}")
    print(f"   Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"   Condition: {description}")
    print(f"   Humidity: {humidity}%")
    print(f"   Wind Speed: {wind_speed} m/s")
    print("-" * 40)

def display_forecast(forecast_data):
    if not forecast_data:
        return

    print("\n📅 5-Day Forecast (Daily at 12:00 PM):\n")

    daily_forecasts = {}

    for item in forecast_data["list"]:
        dt = datetime.datetime.fromtimestamp(item["dt"])
        date_key = dt.strftime("%Y-%m-%d")

        if dt.hour == 12:
            daily_forecasts[date_key] = item

    for date, item in list(daily_forecasts.items())[:5]:
        dt = datetime.datetime.fromtimestamp(item["dt"])
        temp = item["main"]["temp"]
        description = item["weather"][0]["description"].capitalize()

        day_name = dt.strftime("%A")
        formatted_date = dt.strftime("%b %d")

        print(f"{day_name}, {formatted_date}")
        print(f"   {temp}°C - {description}")
        print()

def main():
    print("🌍 Welcome to the Weather Forecast App!\n")

    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    print("\nFetching weather data...")   

    current_data = get_weather(city)
    forecast_data = get_forecast(city)

    display_current_weather(current_data)
    display_forecast(forecast_data)

    print("Thank you for using the Weather App! 🌈")

if __name__ == "__main__":
    main()

    