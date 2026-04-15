#Learning .loc and .iloc attributes in pandas is important for data analysis because they provide a powerful and flexible
#way to select and manipulate data in a DataFrame. They are essential tools for any data analyst working with pandas.
#The challenges below require that you use these attributes in your analysis.
#You will continue to work with the retail_shop_data CSV file.

#5 Using the Seaborn library, create a scatter plot to visualize the relationship between sales and costs for each product.
#Is there any noticeable correlation?

import pandas as pd
import numpy as np

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv('retail_shop_data.csv')

# Calculate total profit for all products
df1['Unit Profit'] = df1['Price'] - df1['Cost']
df1['Total Profit'] = df1['Unit Profit'] * df1['Quantity']

# Sort by Total Profit ascending (least profitable first)
df1_sorted = df1.sort_values('Total Profit').reset_index(drop=True)

# Use .iloc to get the two least profitable products (first two rows)
least_profitable = df1_sorted.iloc[0:2]['Product Name']

# Find the most profitable product's name
max_profit = df1['Total Profit'].max()

# Use .loc to return the full DataFrame subset of the most profitable product
most_profitable = df1.loc[df1['Total Profit'] == max_profit]

# Step 5 - Seaborn scatter plot: Sales (Price) vs Costs
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df1, x='Cost', y='Price', hue='Product Name', s=100)

plt.title('Relationship Between Sales and Costs per Product')
plt.xlabel('Cost')
plt.ylabel('Price (Sales)')
plt.legend(title='Product Name', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

print("\nRetail Shop Data:\n", df1)
print("\nProducts sorted by Total Profit:\n", df1_sorted[['Product Name', 'Total Profit']])
print("\nThe Two Least Profitable Products:\n", least_profitable.values)
print("\nMost Profitable Product DataFrame Subset:\n", most_profitable)
print("\nCorrelation between Cost and Price:", round(df1['Cost'].corr(df1['Price']), 2))