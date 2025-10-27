# from coords_data import Locations
from dotenv import load_dotenv
import requests
import json 
import os

Locations=[{"City":"Delhi", "Lattitude":28.6139, "Longitude":77.2090}]
load_dotenv()

API_KEY = os.getenv("API_KEY")

for loc in Locations:
    City = loc["City"]
    Long = loc["Longitude"]
    Latt = loc["Lattitude"]

    url = f"https://developer.nrel.gov/api/pvwatts/v8.json/?api_key={API_KEY}&lat={Latt}&lon={Long}&system_capacity=3&module_type=0&losses=15&array_type=0&tilt=15&azimuth=180"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        print(json.dumps(data, indent=4))



