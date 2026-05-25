#For this challenge, you are going to preprocess and analyze a dataset of car rental services.
#You are going to use the rental_car_analysis dataset. Here is a snippet of the data below:

#3 Using pandas, fill in the missing values using the column median (numeric columns only).

import pandas as pd

# Load the dataset
df = pd.read_csv('rental_car_analysis.csv')

# Check how many rows are in the dataset
num_rows = df.shape[0]
print("Number of rows in the dataset:", num_rows)

# Check the sum of duplicates in the "City" column
duplicate_cities = df['City'].duplicated().sum()
print("Number of duplicate values in the 'City' column:", duplicate_cities)

# Find missing data in the DataFrame
missing_data = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_data)

# Display rows that contain missing data
rows_with_missing_data = df[df.isnull().any(axis=1)]

print("\nRows with missing data:")
print(rows_with_missing_data)

# Fill missing values using the column median (numeric columns only)
numeric_columns = df.select_dtypes(include='number').columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

# Display updated missing values
print("\nMissing values after filling numeric columns with median:")
print(df.isnull().sum())


