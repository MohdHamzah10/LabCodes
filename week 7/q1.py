import pandas as pd
import numpy as np

df = pd.read_csv("week 7/data.csv")

print("First Five Rows: ")
print(df.head())

print("Last Five Rows: ")
print(df.tail())

print("Dataset Info: ")
print(df.info())
