#In this challenge, you will preprocess and analyze runners data.
#You will import the runners_and_income_data file. This is a CSV file.

#6 Create a subset of the DataFrame by selecting the last two rows of the dataset.
#Reset the index and drop the other index column.
# Save the DataFrame as a CSV file. Name your subset "runners_data_modified.csv." Save it without the index.

import pandas as pd
import numpy as np

df = pd.read_csv("runners_and_income_data.csv")

# Display first 2 rows
print("\nRunners & Income Dataset:\n")
print(df.head(2))

# Display number of rows and columns
print("\nShape of DataFrame:")
print(df.shape)

# Optional: separate rows and columns
rows, columns = df.shape

print("\nNumber of rows:", rows)
print("Number of columns:", columns)

# total NaNs overall
print("\nTotal NaN values in dataset:")
print(df.isna().sum().sum())


#  Drop rows where ALL values are NaN
df = df.dropna(how='all')

#  Replace remaining NaN values with 0.0
df = df.fillna(0.0)

print("\nCleaned DataFrame (first 5 rows):")
print(df.head())


# Calculate total miles run using np.sum
total_miles = np.sum(df["Miles Run"])

print("\nTotal Miles Run by All Names:")
print(total_miles)

# Find people with an income of 50000
income_50000 = df[df["Income"] == 50000]

# Count how many people
count_50000 = income_50000.shape[0]

# Get list of names
names_50000 = income_50000["Name"].tolist()

print("\nNumber of people with income of $50000:")
print(count_50000)

print("\nList of names with income of $50000:")
print(names_50000)

# Create subset with the last two rows
last_two_rows = df.tail(2).reset_index(drop=True)

print("\nLast Two Rows Subset:")
print(last_two_rows)

# Save subset as a CSV file without the index
last_two_rows.to_csv("runners_data_modified.csv", index=False)

print("\nFile saved as 'runners_data_modified.csv'")