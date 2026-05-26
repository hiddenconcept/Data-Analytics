#In this challenge, you will analyze and transform data.
# You will import the cars_and_careers CSV file. Here is a sample of the dataset below:

#1. Import the cars_and_careers dataset.
# Using the pandas describe() method, what is the mean age of the "Age" column?

import pandas as pd

# Load Dataset
df = pd.read_csv('cars_and_careers.csv')

# Mean Age
age_mean = df['Age'].mean()

print("\nCars & Careers Dataset:\n", df.head())

print("\nMean Age:", age_mean)