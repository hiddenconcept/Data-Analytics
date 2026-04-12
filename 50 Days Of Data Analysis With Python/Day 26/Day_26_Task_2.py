# Using pandas, what is the difference in costs between the most profitable product and the least profitable product.

import pandas as pd

df = pd.read_csv('retail_shop_data.csv')
print()
# Calculate profit margin for each row
df["Profit Margin"] = df["Total"] - (df["Cost"] * df["Quantity"])

# Filter for jackets and sneakers
jackets = df[df["Product Name"] == "Jacket"]["Profit Margin"].sum()
sneakers = df[df["Product Name"] == "Sneakers"]["Profit Margin"].sum()

# Calculate the difference
difference = abs(jackets - sneakers)

print(f"Total Profit - Jackets: ${jackets:.2f}")
print(f"Total Profit - Sneakers: ${sneakers:.2f}")
print(f"Difference in Profit: ${difference:.2f}")

# Total profit per product
product_profit = df.groupby("Product Name")["Profit Margin"].sum()

# Find most and least profitable products
most_profitable = product_profit.idxmax()
least_profitable = product_profit.idxmin()

# Get the cost for each
most_profitable_cost = df[df["Product Name"] == most_profitable]["Cost"].sum()
least_profitable_cost = df[df["Product Name"] == least_profitable]["Cost"].sum()

# Calculate the difference
cost_difference = abs(most_profitable_cost - least_profitable_cost)

print(f"\nMost Profitable Product: {most_profitable}")
print(f"Total Cost - {most_profitable}: ${most_profitable_cost:.2f}")

print(f"\nLeast Profitable Product: {least_profitable}")
print(f"Total Cost - {least_profitable}: ${least_profitable_cost:.2f}")

print(f"\nDifference in Costs: ${cost_difference:.2f}")
