
import pandas as pd

df = pd.DataFrame([[12,42,64],[32,55,75],[39,0,33]])

coff = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')

#loc & iloc

#print(coff.loc[1:7,["Day","Units Sold"]])

#loc gives o/p for row =1 to 7  columns as the name in DF

#print(coff.iloc[1:5,[0,1]])

#iloc only numeric in rows and columns row denoted
# as 1:3 and columns as [0,2]
