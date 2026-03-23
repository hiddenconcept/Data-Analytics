#Create a copy of the DataFrame. Add another column to the DataFrame that will convert the kilometers run into miles.

import pandas as pd

df = pd.read_csv ("running_data.csv")

print("\nOriginal DataFrame:\n", df)

df_copy = df.copy()

df_copy['Distance(miles)'] = (df_copy['Distance(km)']*0.621371).round(2)
print("\nUpdated DataFrame:\n", df_copy)