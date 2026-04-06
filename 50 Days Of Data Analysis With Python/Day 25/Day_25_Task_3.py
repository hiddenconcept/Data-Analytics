#Calculate the total cost of products and add this as a column to the DataFrame. Name this column: Costs.
#Calculate the difference between total revenue and total expenses. Name this column: Profit.

import pandas as pd

#setup dataframe for csv
df = pd.read_csv('retail_shop_data.csv')
print("\nFirst 5 Rows:\n",df.head())
print("\nShape of DataFrame (rows,columns):\n",df.shape)
print("\nNumber of Duplicates Rows:\n",df.duplicated().sum())
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