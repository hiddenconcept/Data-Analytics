#Which products have a profit margin of over $15? Use pandas.

import pandas as pd

# Setup dataframe for csv
df = pd.read_csv('retail_shop_data.csv')
print("\nFirst 5 Rows:\n", df.head())
print("\nShape of DataFrame (rows,columns):\n", df.shape)
print("\nNumber of Duplicates Rows:\n", df.duplicated().sum())

# Create a copy of the DataFrame
df_copy = df.copy()

# Rename the specified columns
df_copy = df_copy.rename(columns={
    "Total": "Revenue",
    "Price": "Price Per Product",
    "Cost": "Cost Per Product"
})

# Verify the changes
print("\nRenamed Columns:")
print(df_copy.columns.tolist())

print("\nFirst 5 Rows of Copied DataFrame:\n", df_copy.head())

# Calculate profit margin (Revenue minus total cost)
df_copy["Profit Margin"] = df_copy["Revenue"] - (df_copy["Cost Per Product"] * df_copy["Quantity"])

# Add Filter column: True if profit margin > $15, otherwise False
df_copy["Filter"] = df_copy["Profit Margin"] > 15

# Filter products with a profit margin over $15
high_margin_products = df_copy[df_copy["Profit Margin"] > 15][["Product Name", "Profit Margin"]]

# Verify the new columns
print("\nDataFrame with Profit Margin and Filter columns:")
print(df_copy[["Revenue", "Cost Per Product", "Profit Margin", "Filter"]].head(10))

print("\nProducts with a Profit Margin over $15:\n", high_margin_products)