import pandas as pd
import numpy as np

coff = pd.read_csv('./data/coffee.csv')
bios = pd.read_csv('./data/bios.csv')

a = bios.loc[bios['height_cm']>215,["name","height_cm"]]
a = bios[(bios["height_cm"]>220) &(bios["born_country"] =="USA")] 
print(a.head())

# search using str contains

a = bios[bios["name"].str.contains("sam",case = False)]
print(a.head())
a = bios[bios["born_country"].isin(["USA","FRA"]) &bios["name"].str.startswith("K")]
print(a.head())

# use query to get output

a = bios.query('born_country == "USA" and height_cm >= 200')
print(a.head())
