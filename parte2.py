import pandas as pd

df = pd.read_csv("data/pokemon.csv", index_col="#")

# cancella uno o più colonne del data frame
# df = df.drop(columns=['Legendary'])

# drop di una riga quando manca un dato
# df = df.dropna(subset=['Type 2'])

# sostituzione dei valori vuoti
df = df.fillna({"Type 2": "None"})

# sostituisce dei alori con degli alti
df['Type 1'] = df['Type 1'].replace({"Grass" : "GRASS"})

#standardizzare una colonna
df['Name'] = df['Name'].str.lower()

# Fix del tipo di dato
df["Legendary"] = df["Legendary"].astype(int)

#rimozione dati duplicati
df = df.drop_duplicates()

print(df)