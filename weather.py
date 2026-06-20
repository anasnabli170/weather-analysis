import requests
from datetime import datetime, timedelta
import pandas as pd
import os
import matplotlib.pyplot as plt

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

test = False
while not test:
    town = input("Please enter your hometown:")
    town_url = f"https://geocoding-api.open-meteo.com/v1/search?name={town}&count=10&language=en&format=json"
    response = requests.get(town_url)
    town_data = response.json()
    test = "results" in town_data
    if not test:
        print("Error: Please enter an existing location:")

n = len(town_data["results"])
choices = ""
for i in range(n):
    choices += f"{i + 1}. {town_data['results'][i]['name']}, {town_data['results'][i]['admin1']}, {town_data['results'][i]['country']}\n"
print(choices)

test = False
while not test:
    try:
        x = int(input("Enter a number from the list: "))
        if 1 <= x <= n:
            test = True
        else:
            print("Error: The number should be from the list")
    except ValueError:
        print(("Error: Please enter a number"))

name = town_data["results"][x - 1]["name"]
latitude = town_data["results"][x - 1]["latitude"]
longitude = town_data["results"][x - 1]["longitude"]

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(weather_url)
weather_data = response.json()

daily_data = weather_data["daily"]
df = pd.DataFrame(
    {
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    }
)

df["avg_temp"] = ((df["max_temp"] + df["min_temp"]) / 2).round(1)

print(df)

plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max_temp"], "r-o", label="max_temp")
plt.plot(df["date"], df["min_temp"], "b-o", label="min_temp")
plt.plot(df["date"], df["avg_temp"], "g--", label="avg_temp")

plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title(f"{name} weather - Past 7 days")
plt.legend()
plt.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv("data/your_hometown_weather.csv", index=False)
plt.savefig("data/weather_chart.png")
plt.show()

print(f"maximum temperature:{df['max_temp'].max()}C°")
print(f"minimum temperature:{df['min_temp'].min()}C°")
print(f"average temperature:{df['avg_temp'].mean():.1f}C°")
print("Data saved to data/your_hometown_weather.csv")
