import pandas as pd

df = pd.read_csv("week 7/data.csv")

df = df.dropna()
print(df.head())

df = df[(df['Value'] > 10000000)]
print(df.head())

df = df.drop(columns=['Direction'])
print(df.head())