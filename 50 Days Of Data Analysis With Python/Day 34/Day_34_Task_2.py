#For this challenge, you are going to preprocess and analyze income data.
#You will import a CSV file called income_data. Here is a sample of income data below:

#2 What is Edward’s height?

import pandas as pd

#Load up the dataset
df = pd.read_csv("income_data.csv")

#Display the first 5 rows
print("\nIncome Datset:\n",df.head())

# Find Edward's height
edward_height = df[df["First Name"] == "Edward"]["Height"]

print("\nEdward's Height:\n")
print(edward_height)