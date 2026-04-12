# Using pandas, write code to check the difference in profit between jackets and sneakers.

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
