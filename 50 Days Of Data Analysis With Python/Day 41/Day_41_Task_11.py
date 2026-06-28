#In this challenge, you are going to gain insights and preprocess fictitious population data.
#You will import the population_data file, which is saved in CSV format.

# 11 Which country has the smallest urban population?

import pandas as pd

df = pd.read_csv('population_data.csv')

# Check missing values
missing_values = df.isnull().sum()

print("\nMissing Values by Column:\n", missing_values)

# Count unique countries
unique_countries = df['Country'].nunique()

print("\nNumber of Unique Countries:", unique_countries)

# Find country with the smallest urban population
smallest_urban_country = df.loc[df['Urban Population'].idxmin(), 'Country']
smallest_urban_population = df['Urban Population'].min()

print("\nCountry with the Smallest Urban Population:", smallest_urban_country)
print("Urban Population:", smallest_urban_population)