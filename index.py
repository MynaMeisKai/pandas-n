import pandas as pd
import numpy as np

coff = pd.read_csv('./data/coffee.csv')
#bios = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv')
coff["Price"] = np.where(coff["Coffee Type"]=="Latte" ,3.99,5.99)
#cnew = coff
#here cnew just pointing to the coff DF but we need to
# copy the coff DF, So
 
#copy
#this actually copies the DF to new 

cnew = coff.copy()
cnew["revenue"]=cnew["Units Sold"] * cnew["Price"]

print(cnew.head())

#Rename

cnew = cnew.rename(columns= {"Price":"price"})
print(cnew.head())
