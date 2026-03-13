import pandas as pd

data = [100, 102, 104, 200, 201]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])

print(" prima series:\n",series,"\n")

# .loc  
series.loc["a"] = 200
print("Series iterata con loc:\n",series.loc["a"],"\n")

# .iloc 
print(series.iloc[0])

# itarare 
print("Series con valorimi minori di:")
print(series[series < 105])


