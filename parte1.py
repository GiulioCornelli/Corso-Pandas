import pandas as pd

data = {
    "name": ["Luca", "Anna", "Marco", "Giulia", "Francesco"],
    "eta": [25, 32, 19, 28, 41],
}

df = pd.DataFrame(data, index=["Empl 1", "Empl 2", "Empl 3", "Empl 4", "Empl 5"])

# aggiungere una colonna
df["Job"] = ["cook", "N/A", "Cashier", "N/A", "cook"]

# aggiungere una riga
new_row = pd.DataFrame([{"name":"Sandy", "eta":28,"Job":"Engineer"}], index=["Empl 6"])
df = pd.concat([df,new_row])

print(df)
# print("\n",df.iloc[0])