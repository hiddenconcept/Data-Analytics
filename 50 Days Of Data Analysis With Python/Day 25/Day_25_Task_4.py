#Add another column called "Filter." This column should check for all products that have a profit margin above $15.
#If a product has a profit margin of over $15, it should be given a value of True; otherwise, it should be False.

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

# Verify the new columns
print("\nDataFrame with Profit Margin and Filter columns:")
print(df_copy[["Revenue", "Cost Per Product", "Profit Margin", "Filter"]].head(10))

# Correctly count True/False values in the Filter column
print("\nFilter Value Counts:\n", df_copy["Filter"].value_counts())