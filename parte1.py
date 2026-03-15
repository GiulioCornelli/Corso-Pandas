import pandas as pd

#import csv file 
df = pd.read_csv('data/pokemon.csv')
print(df)

#import json file
df = pd.read_json('data/pokemon.json')
print(df.to_string())