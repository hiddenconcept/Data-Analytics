#In this challenge, you will preprocess and analyze runners data.
#You will import the runners_and_income_data file. This is a CSV file.

#3 What does the describe() method do? Use describe to return the mean of the "Miles Run" column.

import pandas as pd

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

