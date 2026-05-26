#In this challenge, you will analyze and transform data.
# You will import the cars_and_careers CSV file. Here is a sample of the dataset below:

#3. You have come across some new information that must be added to your DataFrame.
#Using pandas shift() and .iloc attributes, insert a row into your DataFrame.
# This row will sit at index 0. The row is: ["Casy", "Ford", 31].
# The last row ["Ben", "Toyota", 55] must be removed.

import pandas as pd

# Load Dataset
df = pd.read_csv('cars_and_careers.csv')

# Shift rows down by 1
df = df.shift(1)

# Insert new row at index 0
df.iloc[0] = ["Casy", "Unknown", 31, "Ford"]

# Remove last row
df = df.iloc[:-1]

# Display updated DataFrame
print("\nUpdated Cars & Careers Dataset:\n")
print(df)