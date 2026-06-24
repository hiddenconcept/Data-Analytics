#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts_expanded.csv dataset.

#5 What is the most profitable and least profitable product?
#What is the difference in profit between the most profitable and the least profitable product?
# By what percentage will the total profit drop if the least profitable product is dropped?

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spare_parts.csv")

# Convert Profit column to numeric
df['total_revenue'] = pd.to_numeric(df['total_revenue'], errors='coerce')

# Calculate total profit by product
product_profit = df.groupby('spare_part')['total_revenue'].sum()

# Most profitable product
most_profitable_product = product_profit.idxmax()
most_profit = product_profit.max()

# Least profitable product
least_profitable_product = product_profit.idxmin()
least_profit = product_profit.min()

# Difference in profit
profit_difference = most_profit - least_profit

# Total profit
total_profit = df['total_revenue'].sum()

# Percentage drop if least profitable product is removed
profit_drop_percentage = (least_profit / total_profit) * 100

# Results
print("Most Profitable Product:", most_profitable_product)
print("Profit:", most_profit)

print("\nLeast Profitable Product:", least_profitable_product)
print("Profit:", least_profit)

print("\nDifference in Profit:", profit_difference)

print("\nProfit drop if least profitable product is removed:",
      profit_drop_percentage, "%")