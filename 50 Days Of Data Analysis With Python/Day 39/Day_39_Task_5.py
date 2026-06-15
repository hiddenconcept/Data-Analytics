#In this challenge, you will analyze and transform data.
# You will import the cars_and_careers CSV file. Here is a sample of the dataset below:

#5. What car does a person by the name of "Emily" drive? And what is her occupation?

import pandas as pd

# Load Dataset
df = pd.read_csv('cars_and_careers.csv')

# Shift rows down by 1
df = df.shift(1)

# Insert new row at index 0
df.iloc[0] = ["Casy", "Unknown", 31, "Ford"]

# Remove last row
df = df.iloc[:-1]

# Find Emily's information
emily = df[df['Name'] == 'Emily']

print("\nEmily:")
print("Car:", emily['Car'].values[0])
print("Occupation:", emily['Occupation'].values[0])
