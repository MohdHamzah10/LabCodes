import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1️⃣ Load Dataset
df = pd.read_csv(r"C:\Users\CSD\Desktop\8th sem\week 9\Mydata.csv")

# 2️⃣ Basic Overview
print(df.shape, "\n")
print(df.info(), "\n")
print(df.head(), "\n")
print("Missing Values:\n", df.isnull().sum())

# 3️⃣ Numeric & Categorical Columns
num_df = df.select_dtypes(include='number')
cat_df = df.select_dtypes(include='object')

# 4️⃣ Numeric Summary & Correlation
print("\nNumeric Summary:\n", num_df.describe())
sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm")
plt.show()

# 5️⃣ Histograms
num_df.hist(figsize=(8,5))
plt.tight_layout()
plt.show()

# 6️⃣ Top Categories
for col in cat_df.columns:
    print(f"\n{col}:\n", df[col].value_counts().head(10))

# 7️⃣ Boxplots
num_df.plot(kind='box', figsize=(8,4))
plt.show()

# 8️⃣ Remove Outliers (IQR)
Q1 = num_df.quantile(0.25)
Q3 = num_df.quantile(0.75)
IQR = Q3 - Q1
df_clean = df[~((num_df < (Q1 - 1.5*IQR)) | (num_df > (Q3 + 1.5*IQR))).any(axis=1)]
print("\nShape after removing outliers:", df_clean.shape)