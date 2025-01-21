import pandas as pd

df = pd.DataFrame([[12,42,64],[32,55,75],[39,0,33]])

coff = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
bios = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv')
# sort ,ascending 

#sort one column
#print(coff.sort_values("Units Sold",ascending=False))

#sort two column
print(coff.sort_values(["Units Sold","Coffee Type"],ascending=[0,1]))
