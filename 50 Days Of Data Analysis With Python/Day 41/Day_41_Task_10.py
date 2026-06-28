#In this challenge, you are going to gain insights and preprocess fictitious population data.
#You will import the population_data file, which is saved in CSV format.

# 10 Which country has the biggest population?

import pandas as pd

df = pd.read_csv('population_data.csv')

# Check missing values
missing_values = df.isnull().sum()

print("\nMissing Values by Column:\n", missing_values)

# Count unique countries
unique_countries = df['Country'].nunique()

print("\nNumber of Unique Countries:", unique_countries)

# Calculate average urban population
average_urban_population = df['Urban Population'].mean()

print("\nAverage Urban Population of All Countries:", average_urban_population)

# Find country with the biggest population
largest_population_country = df.loc[df['Population'].idxmax(), 'Country']
largest_population = df['Population'].max()

print("\nCountry with the Biggest Population:", largest_population_country)
print("Population:", largest_population)