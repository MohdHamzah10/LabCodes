import pandas as pd

df = pd.read_csv("week 7/data.csv")

print(df.head())

df = df.rename(columns={
    'Year':'Calendar Year',
    'Transport_Mode':'Transportation'
})

print(df.dtypes)

df['Calendar Year'] = df['Calendar Year'].astype(int)
df['Date'] = pd.to_datetime(df['Date'],dayfirst=True)

print(df.dtypes)
print(df.head())