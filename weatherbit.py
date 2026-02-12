from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY")

start_date = "2026-02-04"
end_date = "2026-02-04"

url = f"https://api.weatherbit.io/v2.0/current?city={CITY}&start_date={start_date}&end_date={end_date}&key={API_KEY}"
response = requests.request('GET', url)
with open("./weather.txt", "w") as f:
    f.write(response.text)