#For this challenge, you are going to use the sports_data dataset.
#The file is a CSV file. Here is a sample of the dataset below:

#4 Using the pandas method, rename the "Yellow" column to "Yellow Cards."

import pandas as pd

# Load the dataset
df = pd.read_csv('sports_data.csv')

# Rename the "Yellow" column to "Yellow Cards"
df = df.rename(columns={"Yellow": "Yellow Cards"})

# Check the first five rows to confirm the change
print(df.head())