#For this challenge, you are going to preprocess and analyze a dataset of car rental services.
#You are going to use the rental_car_analysis dataset. Here is a snippet of the data below:

#1 Write code to check how many rows are in the dataset. Check the sum of duplicates in the "City" column.

import pandas as pd

# Load the dataset
df = pd.read_csv('rental_car_analysis.csv')

#Check how many rows are in the dataset
num_rows = df.shape[0]
print("Number of rows in the dataset:", num_rows)

# Check the sum of duplicates in the "City" column
duplicate_cities = df['City'].duplicated().sum()
print("Number of duplicate values in the 'City' column:", duplicate_cities)