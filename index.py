import pandas as pd
import numpy as np

df = pd.DataFrame([[12,42,64],[32,55,75],[39,0,33]])

coff = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
bios = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv')
# Add / Remove Columns

coff["Price"] = np.where(coff["Coffee Type"] == "Latte",3.99,5.99)

#print(coff.head(3))

#delete 

#coff.drop(2)
#print(coff.drop(columns=["Units Sold"]))
print(coff.drop(columns=["Units Sold"],inplace= True))
print(coff.head())
