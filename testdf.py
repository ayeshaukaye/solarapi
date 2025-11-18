import pandas as pd

# import excel file 
df = pd.read_excel(r"C:\Users\admin\Documents\s\solarapi\in.xlsx")
df['solrad_annual'] = 0.0
print(df)