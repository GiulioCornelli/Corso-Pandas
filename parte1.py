
import pandas as pd

#import csv file 
df = pd.read_csv('data/pokemon.csv')

# Tutto il data frame
# print(df.mean(numeric_only=True)) #Calcola la media aritmetica dei valori
# print(df.sum(numeric_only=True))  #Calcola la somma totale dei valori degli elementi
# print(df.max(numeric_only=True))  #Restituisce il valore massimo trovato in ogni colonna
# print(df.min(numeric_only=True))  #Restituisce il valore minimo trovato in ogni colonna
# print(df.count())                 #Conta il numero di valori non nulli in ogni colonna

# una singoloa riga
# print(df['HP'].mean())
# print(df['HP'].sum())
# print(df['HP'].max())
# print(df['HP'].min())
# print(df['HP'].count())

group = df.groupby("Type 1") 
print(group["HP"].min())


# Altro tipo di aggregazione estraendo solo un gruppo
print(group.get_group('Fire')['Name'].count())