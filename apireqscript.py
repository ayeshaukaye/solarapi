# from coords_data import Locations
from dotenv import load_dotenv
import requests
import json 
import os

Locations=[{"City":"Delhi", "Lattitude":28.6139, "Longitude":77.2090}]
load_dotenv()

API_KEY = os.getenv("API_KEY")

# for loc in Locations:
#     City = loc["City"]
#     Long = loc["Longitude"]
#     Latt = loc["Lattitude"]

#     url = f"https://developer.nrel.gov/api/pvwatts/v8.json/?api_key={API_KEY}&lat={Latt}&lon={Long}&system_capacity=3&module_type=0&losses=15&array_type=0&tilt=15&azimuth=180"

#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#         print(json.dumps(data, indent=4))

# Source - https://stackoverflow.com/a
# Posted by Muhammad Ismail
# Retrieved 2025-11-11, License - CC BY-SA 4.0

# import pandas library
import pandas as pd

# import excel file 
df = pd.read_excel(r"C:\Users\admin\Documents\s\solarapi\in.xlsx")
df['solrad_annual'] = 0.0 #9
df['ac_annual'] = 0.0
df['capacity_factor'] = 0.0

print(df.head())

for i in range(6):
    lat = df.iloc[i,1]
    long = df.iloc[i,2]
    url = f"https://developer.nrel.gov/api/pvwatts/v8.json/?api_key={API_KEY}&lat={lat}&lon={long}&system_capacity=3&module_type=0&losses=15&array_type=0&tilt=15&azimuth=180"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(data["outputs"])
        print(f"-------{i}--------")
        # print(json.dumps(data["outputs"], indent=4))
    df.iloc[i,9] = data["outputs"]["solrad_annual"]
    df.iloc[i,10] = data["outputs"]["ac_annual"] # getting value of each row of column 3 multiply it with 2 and store it on same row index in column 3 in datafram
    df.iloc[i,11] = data["outputs"]["capacity_factor"] # getting value of each row of column 3 multiply it with 2 and store it on same row index in column 3 in datafram

# df.to_csv('sales.xlsx') #now save the updated dataframe to same name of excel file
print(df) #enter code here


