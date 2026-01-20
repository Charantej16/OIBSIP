import requests

def fetch_current_weather(location_name):
    secret_key = "caabe8884a09ec446ecce987390a8a08"
    endpoint = "https://openweathermap.org/find?utf8=%E2%9C%93&q=hyderabad"

    query_data = {
        "q": location_name,
        "appid": secret_key,
        "units": "metric"
    }

    try:
        server_response = requests.get(endpoint, params=query_data, timeout=10)

        if server_response.status_code != 200:
            print("\n⚠️ Unable to fetch weather details.")
            print("Please check city name or API key.\n")
            return

        weather_info = server_response.json()

        city = weather_info.get("name")
        temp = weather_info["main"]["temp"]
        humidity = weather_info["main"]["humidity"]
        condition = weather_info["weather"][0]["main"]

        print("\n====== WEATHER REPORT ======")
        print(f"Location    : {city}")
        print(f"Temperature : {temp} °C")
        print(f"Humidity    : {humidity} %")
        print(f"Condition   : {condition}")
        print("============================\n")

    except requests.exceptions.RequestException:
        print("\n❌ Network error occurred. Try again later.\n")


def start_application():
    user_city = input("Enter city name: ").strip()
    if user_city:
        fetch_current_weather(user_city)
    else:
        print("City name cannot be empty.")


start_application()


