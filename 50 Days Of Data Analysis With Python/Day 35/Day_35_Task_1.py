#In this challenge, you will preprocess and analyze runners data.
#You will import the runners_and_income_data file. This is a CSV file.

#1 Load the dataset using pandas and view the first two rows of the dataset.
#You want to know how many rows and columns are in the DataFrame; write a code to check the number of rows and columns.

import pandas as pd

df = pd.read_csv("runners_and_income_data.csv")

# Display first 2 rows
print("\nRunners & Income Dataset:\n")
print(df.head(2))

# Display number of rows and columns
print("\nShape of DataFrame:")
print(df.shape)

# Optional: separate rows and columns
rows, columns = df.shape

print("\nNumber of rows:", rows)
print("Number of columns:", columns)