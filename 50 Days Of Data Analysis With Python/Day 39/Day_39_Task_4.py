#In this challenge, you will analyze and transform data.
# You will import the cars_and_careers CSV file. Here is a sample of the dataset below:

#4. Using the pandas.str.find() method,
# write a code to confirm if the name "Ben" has been removed from the DataFrame.

import pandas as pd

# Load Dataset
df = pd.read_csv('cars_and_careers.csv')

# Shift rows down by 1
df = df.shift(1)

# Insert new row at index 0
df.iloc[0] = ["Casy", "Unknown", 31, "Ford"]

# Remove last row
df = df.iloc[:-1]

if 'Ben' in df['Name'].values:
    print("Ben is still in the DataFrame...")
else:
    print("Ben has been removed from the DataFrame!")
