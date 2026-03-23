import pandas as pd

df = pd.read_csv ("running_data.csv")

print("\nOriginal DataFrame:\n", df)
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe())