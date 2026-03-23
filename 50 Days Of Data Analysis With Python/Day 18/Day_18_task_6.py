#Using the pandas.Series.map() function, create a subset of the DataFrame with runners that covered over 5 miles.
#Reset the index of the resulting DataFrame and ensure to drop the index column. Which runner covered the most distance?

import pandas as pd

df = pd.read_csv("running_data.csv")
print("\nOriginal DataFrame:\n", df)

df_copy = df.copy()

# Convert km to miles
df_copy['Distance(miles)'] = (df_copy['Distance(km)'] * 0.621371).round(2)

# Calculate speed in km per hour
df_copy['Speed(km/h)'] = (df_copy['Distance(km)'] / df_copy['Time(Hours)']).round(2)

# Load and merge rest data
df_rest = pd.read_csv("runner_test.csv")
print("\nAddition DataFrame:\n", df_rest)

df_merged = df_copy.merge(df_rest, left_on='Name', right_on='Runners', how='left')
df_merged.drop(columns=['Runners'], inplace=True)

df_merged['Rest Time(Hrs)'] = df_merged['Rest time(Mins)'].apply(lambda x: round(x / 60, 2) if pd.notna(x) else x)
print("\nFinal DataFrame:\n", df_merged)

# Filter runners who covered over 5 miles using map()
over_5_miles = df_merged[df_merged['Distance(miles)'].map(lambda x: x > 5)]

# Reset index and drop the old index column
over_5_miles = over_5_miles.reset_index(drop=True)

print("\nRunners who covered over 5 miles:\n", over_5_miles)

# Find the runner who covered the most distance
most_distance = over_5_miles.loc[over_5_miles['Distance(miles)'].idxmax()]
print("\nRunner who covered the most distance:")
print(most_distance[['Name', 'Distance(miles)']])

