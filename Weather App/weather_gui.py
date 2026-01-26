import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "88a58de1771af9381f4040dc2c9a471c"


def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 401:
            messagebox.showerror("Error", "Invalid API Key")
            return

        if response.status_code == 404:
            messagebox.showerror("Error", "City not found")
            return

        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()

        result_label.config(
            text=f"📍 {city}\n\n"
                 f"🌡 Temperature: {temp} °C\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"☁️ Condition: {condition}"
        )

    except requests.exceptions.ConnectionError:
        messagebox.showerror(
            "Network Error",
            "Internet connection blocked.\nTry using mobile hotspot."
        )
    except requests.exceptions.Timeout:
        messagebox.showerror("Timeout", "Server is taking too long to respond")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- GUI DESIGN ----------

app = tk.Tk()
app.title("Weather App")
app.geometry("420x450")
app.resizable(False, False)
app.configure(bg="#eef6ff")

# Header
tk.Label(
    app,
    text="Weather Application",
    font=("Segoe UI", 20, "bold"),
    bg="#eef6ff",
    fg="#1c3f60"
).pack(pady=20)

# Card
card = tk.Frame(app, bg="white", bd=0)
card.pack(padx=20, pady=10, fill="both", expand=True)

# City input
tk.Label(
    card,
    text="Enter City Name",
    font=("Segoe UI", 12),
    bg="white"
).pack(pady=(25, 5))

city_entry = tk.Entry(
    card,
    font=("Segoe UI", 12),
    width=25,
    bd=2,
    relief="groove"
)
city_entry.pack(pady=5)

# Button
tk.Button(
    card,
    text="Get Weather",
    font=("Segoe UI", 12, "bold"),
    bg="#1c3f60",
    fg="white",
    activebackground="#16324d",
    relief="flat",
    padx=15,
    pady=6,
    command=get_weather
).pack(pady=15)

# Result
result_label = tk.Label(
    card,
    text="🌤 Weather details will appear here",
    font=("Segoe UI", 11),
    bg="white",
    fg="#444",
    justify="left"
)
result_label.pack(pady=20)

# Footer
tk.Label(
    app,
    text="Powered by OpenWeather API",
    font=("Segoe UI", 9),
    bg="#eef6ff",
    fg="#666"
).pack(pady=10)

app.mainloop()
