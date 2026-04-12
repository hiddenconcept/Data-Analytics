# Using Matplotlib, create a bar stack plot of the sales, costs, and profits of the 6 least profitable products.
# The bar plot should be sorted by profit in ascending order.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('retail_shop_data.csv')

# Calculate profit margin for each row
df["Profit Margin"] = df["Total"] - (df["Cost"] * df["Quantity"])

# Aggregate sales, costs, and profits by product
product_stats = df.groupby("Product Name").agg(
    Sales=("Total", "sum"),
    Costs=("Cost", "sum"),
    Profit=("Profit Margin", "sum")
).reset_index()

# Get the 6 least profitable products, sorted by profit ascending
least_profitable_6 = product_stats.nsmallest(6, "Profit").sort_values("Profit", ascending=True)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(least_profitable_6["Product Name"], least_profitable_6["Sales"], label="Sales", color="steelblue")
ax.bar(least_profitable_6["Product Name"], least_profitable_6["Costs"], label="Costs", color="tomato", bottom=least_profitable_6["Sales"])
ax.bar(least_profitable_6["Product Name"], least_profitable_6["Profit"], label="Profit", color="mediumseagreen", bottom=least_profitable_6["Sales"] + least_profitable_6["Costs"])

ax.set_title("6 Least Profitable Products: Sales, Costs & Profit")
ax.set_xlabel("Product Name")
ax.set_ylabel("Amount ($)")
ax.legend()
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()