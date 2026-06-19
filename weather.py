import requests
from datetime import datetime,timedelta
import pandas as pd
import os

today=datetime.now()
week_ago=today-timedelta(days=7)

start_date=week_ago.strftime("%Y-%m-%d")
end_date=today.strftime("%Y-%m-%d")

town=input("Please enter your hometown:")

town_url=f"https://geocoding-api.open-meteo.com/v1/search?name={town}&count=10&language=en&format=json"
response=requests.get(town_url)
town_data=response.json()
print(town_data)

latitude=town_data['results'][0]['latitude']
longitude=town_data['results'][0]['longitude']

weather_url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response=requests.get(weather_url)
weather_data=response.json()
print (weather_data)

daily_data=weather_data['daily']
df=pd.DataFrame({
  'date':daily_data['time'],
  'max_temp':daily_data['temperature_2m_max'],
  'min_temp':daily_data['temperature_2m_min']
})

df['avg_temp']=(df['max_temp']+df['min_temp'])/2

print(df)

if not os.path.exists('data'):
  os.makedirs('data')

df.to_csv('data/your_hometown_weather.csv',index=False)
print(f"average temperature:{df['avg_temp'].mean():.1f}C°")
print("Data saved to data/your_hometown_weather.csv")