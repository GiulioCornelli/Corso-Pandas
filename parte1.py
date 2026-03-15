import pandas as pd

#import csv file 
df = pd.read_csv('data/pokemon.csv', index_col='#')

#primo filtraggio
# hp80 = df[df['HP'] == 80]
# print(hp80)

type = df[(df['Type 1'] == "Fire") & (df['Type 2'] == "Dragon")]
print(type)