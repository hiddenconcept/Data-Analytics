#. You have come across some more information to be added to the DataFrame. Some runners stopped for a rest.
#This information is saved in a CSV dataset called "runner_rest."

#Merge this dataset into your DataFrame above. Use the pandas merge() method.
#Ensure to drop the "Runners" column since you already have the "Names" column.

import pandas as pd

df = pd.read_csv ("running_data.csv")

print("\nOriginal DataFrame:\n", df)

df_copy = df.copy()

# Convert km to miles
df_copy['Distance(miles)'] = (df_copy['Distance(km)']*0.621371).round(2)

# Calculate speed in km per hour
df_copy['Speed(km/h)'] = (df_copy['Distance(km)'] / df_copy['Time(Hours)']).round(2)

#Load rest of data
df_rest = pd.read_csv ("runner_test.csv")
print("\nAddition DataFrame:\n", df_rest)

df_merged = df_copy.merge(df_rest,left_on='Name', right_on='Runners', how='left')

df_merged.drop(columns=['Runners'], inplace=True)

print("\nMerge DataFrame:\n", df_merged)

