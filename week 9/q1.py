import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\CSD\Desktop\8th sem\week 9\Mydata.csv")

# Boxplot
df.boxplot()
plt.show()

def remove_outliers(df):
    num_df = df.select_dtypes(include='number')  # only numbers
    
    Q1 = num_df.quantile(0.25)
    Q3 = num_df.quantile(0.75)
    IQR = Q3 - Q1

    mask = ~((num_df < (Q1 - 1.5*IQR)) | (num_df > (Q3 + 1.5*IQR))).any(axis=1)
    
    return df[mask]

df = remove_outliers(df)
print("OUTLIERS REMOVED")
print(df.head())