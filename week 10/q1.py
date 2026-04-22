import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("week 7/data.csv")

#df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

print(df.head())

plt.figure(figsize=(10,5))
plt.plot(df['Year'], df['Value'], marker='x', color='green')

plt.title("Exports Over Time")
plt.xlabel("Date")
plt.ylabel("Export Value")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()


order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

df['Weekday'] = pd.Categorical(df['Weekday'], categories=order, ordered=True)

weekday_data = df.groupby('Weekday')['Value'].mean().reindex(order)

plt.figure(figsize=(8,5))
weekday_data.plot(kind='bar', color='red')

plt.title("Average Exports by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Average Value")
plt.xticks(rotation=45)

plt.show()