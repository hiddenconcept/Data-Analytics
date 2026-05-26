#In this challenge, you will analyze and transform data.
# You will import the cars_and_careers CSV file. Here is a sample of the dataset below:

#2. Using the pandas transform() method, convert the items in the "cars" column into lowercase letters.

import pandas as pd

# Load Dataset
df = pd.read_csv('cars_and_careers.csv')

# Mean Age
age_mean = df['Age'].mean()

print("\nCars & Careers Dataset:\n", df.head())

# Convert "cars" column to lowercase using transform()
df['cars'] = df['Car'].transform(lambda x: x.lower())

# Display first 5 rows
print("\nCars & Careers Dataset:\n", df.head())