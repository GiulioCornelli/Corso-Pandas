import pandas as pd

#import csv file 
df = pd.read_csv('data/pokemon.csv')

# selet colum
print(df["name"])
