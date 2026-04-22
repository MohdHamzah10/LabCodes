import pandas as pd

df = pd.read_csv(r"C:\Users\CSD\Desktop\8th sem\week 10\dat.csv")

if(df['salary'].isnull().any()):
    print("Missing values found in 'salary' column. Filling with mean.")
    df['salary'].fillna(df['salary'].mean(), inplace=True)

print(df.head())