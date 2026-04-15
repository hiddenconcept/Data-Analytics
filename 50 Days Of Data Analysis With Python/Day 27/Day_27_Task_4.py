#Learning .loc and .iloc attributes in pandas is important for data analysis because they provide a powerful and flexible
#way to select and manipulate data in a DataFrame. They are essential tools for any data analyst working with pandas.
#The challenges below require that you use these attributes in your analysis.
#You will continue to work with the retail_shop_data CSV file.

#4 Using the .loc attribute, return a DataFrame subset of the most profitable product.

import pandas as pd
import numpy as np

df1 = pd.read_csv('retail_shop_data.csv')

# Calculate total profit for all products
df1['Unit Profit'] = df1['Price'] - df1['Cost']
df1['Total Profit'] = df1['Unit Profit'] * df1['Quantity']

# Sort by Total Profit ascending (least profitable first)
df1_sorted = df1.sort_values('Total Profit').reset_index(drop=True)

# Use .iloc to get the two least profitable products (first two rows)
least_profitable = df1_sorted.iloc[0:2]['Product Name']

# Step 4 - Find the most profitable product's name
max_profit = df1['Total Profit'].max()

# Use .loc to return the full DataFrame subset of the most profitable product
most_profitable = df1.loc[df1['Total Profit'] == max_profit]

print("\nRetail Shop Data:\n", df1)
print("\nProducts sorted by Total Profit:\n", df1_sorted[['Product Name', 'Total Profit']])
print("\nThe Two Least Profitable Products:\n", least_profitable.values)
print("\nMost Profitable Product DataFrame Subset:\n", most_profitable)

