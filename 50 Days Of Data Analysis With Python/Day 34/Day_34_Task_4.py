#For this challenge, you are going to preprocess and analyze income data.
#You will import a CSV file called income_data. Here is a sample of income data below:

#4 What is the average income per female?

import pandas as pd

#Load up the dataset
df = pd.read_csv("income_data.csv")

#Display the first 5 rows
print("\nIncome Datset:\n",df.head())


# Create a subset DataFrame with only female names
female_df = df[df["Gender"] == "F"]

# Reset the index and drop the old index column
female_df = female_df.reset_index(drop=True)

print("\nFemale Subset DataFrame:\n")
print(female_df)

# Calculate the average income for females
average_female_income = female_df["Income"].mean()

print("\nAverage Female Income:\n", average_female_income)