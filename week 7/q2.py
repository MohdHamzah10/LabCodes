import pandas as pd
import numpy as np

# Example DataFrame
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45],
    'C': [2, 4, 6, 8, 10],
    'D': [1, 3, 5, 7, 9]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

avg_second_column = df.iloc[:,1].mean()
print("Average of second column:", avg_second_column)

avg_3_4 = df.iloc[:5, 2:4].mean()
print("Average of first 5 rows (3rd and 4th columns):\n", avg_3_4)

row_sum = df.sum(axis=1)
print("Row-wise sum:\n", row_sum)

row_avg = df.mean(axis=1)
max_row_avg = row_avg.max()

print("Row averages:\n", row_avg)
print("Maximum of row averages:", max_row_avg)