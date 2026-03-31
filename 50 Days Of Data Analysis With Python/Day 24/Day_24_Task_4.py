#Write a code to return the value of sales between 11-20- 2021 and 12-06-2021.
#Create a DataFrame and return the total sales value for this period.

import pandas as pd

df = pd.read_excel('Asset_sales_data.xlsx')

# Strip hidden spaces from column names (safety check)
df.columns = df.columns.str.strip()

# View the first 5 rows
print("\nFirst 5 rows:\n", df.head())

# Return the data types
print("\nData Types of All Columns:\n", df.dtypes)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# ── Filter sales between 2021-11-20 and 2021-12-06
start_date = '2021-11-20'
end_date = '2021-12-06'

filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

print(f"\nSales between {start_date} and {end_date}:\n")
print(filtered_df)

# Total sales for this period
total_sales = filtered_df['sales'].sum()
print(f"\nTotal Sales ({start_date} to {end_date}): ${total_sales:,.2f}")