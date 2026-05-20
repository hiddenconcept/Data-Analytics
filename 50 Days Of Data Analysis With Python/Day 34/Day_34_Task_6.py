#For this challenge, you are going to preprocess and analyze income data.
#You will import a CSV file called income_data. Here is a sample of income data below:

#6 What is the average income of males over 50 compared to the average salary of females over 50?
# Plot a bar plot using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

# Load up the dataset
df = pd.read_csv("income_data.csv")

# Display the first 5 rows
print("\nIncome Dataset:\n", df.head())

# Create subsets for males and females over 50
males_over_50 = df[(df["Gender"] == "M") & (df["Age"] > 50)]
females_over_50 = df[(df["Gender"] == "F") & (df["Age"] > 50)]

# Calculate average incomes
male_avg_income = males_over_50["Income"].mean()
female_avg_income = females_over_50["Income"].mean()

# Print averages
print("\nAverage Male Income Over 50:\n", male_avg_income)
print("\nAverage Female Income Over 50:\n", female_avg_income)

# Create bar plot
groups = ["Males Over 50", "Females Over 50"]
averages = [male_avg_income, female_avg_income]

plt.bar(groups, averages)

# Add labels and title
plt.xlabel("Groups")
plt.ylabel("Average Income")
plt.title("Average Income Comparison Over 50")

# Display plot
plt.show()