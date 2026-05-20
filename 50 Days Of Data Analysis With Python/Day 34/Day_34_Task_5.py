#For this challenge, you are going to preprocess and analyze income data.
#You will import a CSV file called income_data. Here is a sample of income data below:

#5 Your boss suspects that there is a correlation between the person's age and their income.
#She asks you to create a plot) to show this correlation.
# Using Pandas and Matplotlib, create a scatter plot of age against income.

import pandas as pd
import matplotlib.pyplot as plt

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

# Create scatter plot of Age vs Income
plt.scatter(df["Age"], df["Income"])

# Add labels and title
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Age vs Income")

# Display the plot
plt.show()