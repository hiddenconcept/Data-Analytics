#For this challenge, you are going to preprocess and analyze income data.
#You will import a CSV file called income_data. Here is a sample of income data below:

#1. Using pandas, write a code to display only 5 rows from the data. How many males and females are in the dataset?

import pandas as pd

#Load up the dataset
df = pd.read_csv("income_data.csv")

#Display the first 5 rows
print("\nIncome Datset:\n",df.head())

# Count males and females
print("\nGender Count:\n")
print(df['gender'].value_counts())