#For this challenge, you are going to preprocess and analyze income data.
#You will import a CSV file called income_data. Here is a sample of income data below:

#3 Write another code to create a subset DataFrame of only
# female names from the DataFrame above. Reset the index and drop it as a column.

import pandas as pd

#Load up the dataset
df = pd.read_csv("income_data.csv")

#Display the first 5 rows
print("\nIncome Datset:\n",df.head())


# Create a subset DataFrame with only female names
female_df = df[df["Gender"] == "Female"]

# Reset the index and drop the old index column
female_df = female_df.reset_index(drop=True)

print("\nFemale Subset DataFrame:\n")
print(female_df)