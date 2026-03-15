import pandas as pd

#import csv file 
df = pd.read_csv('data/pokemon.csv', index_col=['Name'])

# selet colum
# print(df['Type 1'])

#selezione multipla
# print(df[['Type 1','Type 2']])

#selezione di una riga/righe
print(df.loc['Charizard'])
print(df.loc['Charmander':'Blastoise']) # da chiave a chiave
print(df.iloc[0:11]) # gli estremi sono esclusi
print(df.iloc[0:11:2, 0:3])# muovendosi ogni 2 e prendendo le prite 3 colonne

# Esercizio
print("---------")
pokemon = input("Inserisci il nome del Pokemon: ")

try:
    print("Pokemon Sceloto:")
    print(df.loc[pokemon])
except:
    print("Il pokemon non è presete")