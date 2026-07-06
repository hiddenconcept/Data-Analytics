#For this challenge, you are going to use the sports_data dataset.
#The file is a CSV file. Here is a sample of the dataset below:

#6. Save the new DataFrame as a CSV file. Give it a name of your choice.

import pandas as pd

# Load the dataset
df = pd.read_csv('sports_data.csv')

# Rename the "Yellow" column to "Yellow Cards"
df = df.rename(columns={"Yellow": "Yellow Cards"})

# Create subset of players with over six fouls
fouls_subset = df.query("Fouls > 6")

# Reset index and remove the old index column
fouls_subset = fouls_subset.reset_index(drop=True)

# Save the new DataFrame as a CSV file
fouls_subset.to_csv("players_over_six_fouls.csv", index=False)

# Display the result
print(fouls_subset.head())
print()
print("File Successfully Saved!")