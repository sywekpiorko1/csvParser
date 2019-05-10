import pandas as pd

df = pd.read_csv("avocado.csv")
# df = pd.read_csv("id4106ip54.csv")

print(df["AveragePrice"].head())
print(df["AveragePrice"].tail())