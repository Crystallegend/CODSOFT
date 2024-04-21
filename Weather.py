import customtkinter as ctk
import requests as re
API_KEY = "" #Enter your OpenWeatherMap API Key

def get_time(seconds):
    remaining_seconds = seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    minutes = (remaining_seconds % 3600) // 60
    second = remaining_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{second:02d}"

def get_weather():
    city = s_name.get()
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    weather = re.get(URL).json()

    if weather["cod"] == "400":
        error.configure(text="No City Entered", text_color="red")
    elif weather["cod"] == "404":
        error.configure(text="No City Found", text_color="red")
    else:
        s_status.configure(text=weather["weather"][0]["main"])
        s_description.configure(text=weather["weather"][0]["description"])
        s_temperature.configure(text=str(weather["main"]["temp"])+" °C")
        s_feel.configure(text=str(weather["main"]["feels_like"])+" °C")
        s_humidity.configure(text=str(weather["main"]["humidity"])+" %")
        s_wind.configure(text=str(weather["wind"]["speed"])+" m/s")
        s_country.configure(text=weather["sys"]["country"])
        s_sunrise.configure(text=get_time(weather["sys"]["sunrise"])+" UTC")
        s_sunset.configure(text=get_time(weather["sys"]["sunset"])+" UTC")
        error.configure(text="")
        return
    
    s_status.configure(text="")
    s_description.configure(text="")
    s_temperature.configure(text="")
    s_feel.configure(text="")
    s_humidity.configure(text="")
    s_wind.configure(text="")
    s_country.configure(text="")
    s_sunrise.configure(text="")
    s_sunset.configure(text="")

def copy_data():
    data = f'''status: {s_status.cget("text")},
    description: {s_description.cget("text")},
    temperature: {s_temperature.cget("text")},
    feel: {s_feel.cget("text")},
    humidity: {s_humidity.cget("text")},
    wind: {s_wind.cget("text")},
    country: {s_country.cget("text")},
    sunrise: {s_sunrise.cget("text")}
    sunset: {s_sunset.cget("text")}'''

    app.clipboard_append(data)
    error.configure(text="Data Copied", text_color="green")


ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Weather App")
app.geometry("500x400")

status = ctk.CTkLabel(app, text="Status: ")
description = ctk.CTkLabel(app, text="Description: ")
temperature = ctk.CTkLabel(app, text="Temperature: ")
feel = ctk.CTkLabel(app, text="Feels like: ")
humidity = ctk.CTkLabel(app, text="Humidity: ")
wind = ctk.CTkLabel(app, text="Wind Speed: ")
country = ctk.CTkLabel(app, text="Country: ")
sunrise = ctk.CTkLabel(app, text="Sunrise: ")
sunset = ctk.CTkLabel(app, text="Sunset: ")
name = ctk.CTkLabel(app, text="Enter City Name: ")

s_status = ctk.CTkLabel(app, text = "", text_color="green")
s_description = ctk.CTkLabel(app, text = "", text_color="green")
s_temperature = ctk.CTkLabel(app, text = "", text_color="green")
s_feel = ctk.CTkLabel(app, text = "", text_color="green")
s_humidity = ctk.CTkLabel(app, text = "", text_color="green")
s_wind = ctk.CTkLabel(app, text = "", text_color="green")
s_country = ctk.CTkLabel(app, text = "", text_color="green")
s_sunrise = ctk.CTkLabel(app, text = "", text_color="green")
s_sunset = ctk.CTkLabel(app, text = "", text_color="green")
s_name = ctk.CTkEntry(app, placeholder_text="City")

status.grid(row=0, column=0, padx=5, pady=5)
description.grid(row=1, column=0, padx=5, pady=5)
temperature.grid(row=2, column=0, padx=5, pady=5)
feel.grid(row=3, column=0, padx=5, pady=5)
humidity.grid(row=4, column=0, padx=5, pady=5)
wind.grid(row=0, column=2, padx=5, pady=5)
country.grid(row=1, column=2, padx=5, pady=5)
sunrise.grid(row=2, column=2, padx=5, pady=5)
sunset.grid(row=3, column=2, padx=5, pady=5)
name.grid(row=5, column=1, padx=5, pady=5)

s_status.grid(row=0, column=1, padx=5, pady=5)
s_description.grid(row=1, column=1, padx=5, pady=5)
s_temperature.grid(row=2, column=1, padx=5, pady=5)
s_feel.grid(row=3, column=1, padx=5, pady=5)
s_humidity.grid(row=4, column=1, padx=5, pady=5)
s_wind.grid(row=0, column=3, padx=5, pady=5)
s_country.grid(row=1, column=3, padx=5, pady=5)
s_sunrise.grid(row=2, column=3, padx=5, pady=5)
s_sunset.grid(row=3, column=3, padx=5, pady=5)
s_name.grid(row=5, column=2, padx=5, pady=5)

get_data = ctk.CTkButton(app, text="Get Data", font=("Arial", 14), command=get_weather)
copy = ctk.CTkButton(app, text="Copy Data", font=("Arial", 14), command=copy_data, fg_color="green")
copy.grid(row=7, column=1, columnspan=2, padx=10)
get_data.grid(row=6, column=1, columnspan=2, padx=20, pady=10)
error = ctk.CTkLabel(app, text="")
error.grid(row=8, column=1, columnspan=2, padx=5, pady=10)

app.mainloop()