#For this challenge, you are going to use the sports_data dataset.
#The file is a CSV file. Here is a sample of the dataset below:

#5 Using the pandas query() method, create a subset DataFrame of only players that got over six fouls.
# Reset your index (set it back to the default 0, 1, 2, etc.) and ensure that you remove the index as a column.

import pandas as pd

# Load the dataset
df = pd.read_csv('sports_data.csv')

# Rename the "Yellow" column to "Yellow Cards"
df = df.rename(columns={"Yellow": "Yellow Cards"})

# Create subset of players with over six fouls
fouls_subset = df.query("Fouls > 6")

# Reset index and remove the old index column
fouls_subset = fouls_subset.reset_index(drop=True)

# Display the result
print(fouls_subset.head())