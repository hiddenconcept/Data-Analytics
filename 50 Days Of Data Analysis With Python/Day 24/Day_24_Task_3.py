#Using pandas, what month had the highest value of sales?

import pandas as pd

df = pd.read_excel('Asset_sales_data.xlsx')

# View the first 5 rows
print("\nFirst 5 rows:\n", df.head())

# Return the data types
print("\nData Types of All Columns:\n", df.dtypes)

# Convert date column to datetime
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

# Extract the month from the date column
df['month'] = df['Sale_Date'].dt.month_name()

# Group by month and sum the sales values
monthly_sales = df.groupby('month')['Sales'].sum()
print("\nTotal Sales Per Month:\n", monthly_sales)

# Find the month with the highest sales
highest_month = monthly_sales.idxmax()
highest_value = monthly_sales.max()
print(f"\nMonth with Highest Sales: {highest_month} (${highest_value:,.2f})")