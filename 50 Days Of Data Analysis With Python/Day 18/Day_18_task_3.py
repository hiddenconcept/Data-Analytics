#Add another column to the DataFrame to calculate the speed per hour in kilometers.

import pandas as pd

df = pd.read_csv ("running_data.csv")

print("\nOriginal DataFrame:\n", df)

df_copy = df.copy()

# Convert km to miles
df_copy['Distance(miles)'] = (df_copy['Distance(km)']*0.621371).round(2)

# Calculate speed in km per hour
df_copy['Speed(km/h)'] = (df_copy['Distance(km)'] / df_copy['Time(Hours)']).round(2)

print("\nUpdated DataFrame:\n", df_copy)