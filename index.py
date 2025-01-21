
import pandas as pd

df = pd.DataFrame([[12,42,64],[32,55,75],[39,0,33]])

coff = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')

#at & iat

print(coff)
print(coff.at[1,"Units Sold"])

#iat rows and columns must be in numerics
print(coff.iat[0,2])
#at and iat only gives exact single output 
#not multiple
