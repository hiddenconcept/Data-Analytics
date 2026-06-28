#In this challenge, you are going to gain insights and preprocess fictitious population data.
#You will import the population_data file, which is saved in CSV format.

# 8  What is the average population of all the countries?

import pandas as pd

df = pd.read_csv('population_data.csv')

# Check missing values
missing_values = df.isnull().sum()

print("\nMissing Values by Column:\n", missing_values)

# Count unique countries
unique_countries = df['Country'].nunique()

print("\nNumber of Unique Countries:", unique_countries)

# Find population range
population_min = df['Population'].min()
population_max = df['Population'].max()

population_range = population_max - population_min

print("\nMinimum Population:", population_min)
print("Maximum Population:", population_max)
print("Population Range:", population_range)

# Calculate mean and median population
population_mean = df['Population'].mean()
population_median = df['Population'].median()

# Calculate average population
average_population = df['Population'].mean()

print("\nAverage Population of All Countries:", average_population)