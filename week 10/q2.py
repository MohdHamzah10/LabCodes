import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("week 7/data.csv")

plt.figure(figsize=(6,5))
plt.scatter(df['Value'], df['Cumulative'], color='green')

plt.title("Value vs Cumulative")
plt.xlabel("Daily Export Value")
plt.ylabel("Cumulative Export")

plt.show()

#corr = df[['Year', 'Value', 'Cumulative']].corr()

plt.figure(figsize=(8,6))
sns.heatmap(df, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()