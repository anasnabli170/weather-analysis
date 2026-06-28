# Hometown Weather Analysis

A Python script that fetches real-time weather data for any city in the world and visualizes the temperature trends over the past 7 days.

## Features

- Searches for any city using the Open-Meteo Geocoding API
- Lets the user select their exact location from a list of results
- Fetches daily max, min, and computes average temperature for the past 7 days
- Visualizes the three temperature trends in a line chart using Matplotlib
- Saves the data as a CSV and the chart as a PNG

## How to Run

1. Clone the repository
2. Install dependencies:
```
pip install requests pandas matplotlib
```
3. Run the script:
```
python main.py
```
4. Enter your city name and select your location from the list

## Libraries Used

- [Requests](https://requests.readthedocs.io/) — fetching data from the Open-Meteo API
- [Pandas](https://pandas.pydata.org/) — structuring and computing temperature data
- [Matplotlib](https://matplotlib.org/) — visualizing temperature trends

## APIs Used

- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) — city search
- [Open-Meteo Forecast API](https://open-meteo.com/en/docs) — historical weather data
