#Use pandas to create a pivot table and calculate the sum of the sales column grouped by the products column.
# Use pandas and Matplotlib to plot this on a bar plot.
#Your plot size must be: width = 12, height = 10.
#Your plot title will be "Total Sales Per Product.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Asset_sales_data.xlsx')

# Strip hidden spaces from column names (safety check)
df.columns = df.columns.str.strip()

# View the first 5 rows
print("\nFirst 5 rows:\n", df.head())

# Return the data types
print("\nData Types of All Columns:\n", df.dtypes)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter sales between 2021-11-20 and 2021-12-06
start_date = '2021-11-20'
end_date = '2021-12-06'

filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

print(f"\nSales between {start_date} and {end_date}:\n")
print(filtered_df)

# Total sales for this period
total_sales = filtered_df['sales'].sum()
print(f"\nTotal Sales ({start_date} to {end_date}): ${total_sales:,.2f}")

# Pivot table: sum of sales grouped by products
pivot_table = pd.pivot_table(
    df,
    values='sales',
    index='products',
    aggfunc='sum'
)

print("\nPivot Table - Total Sales Per Product:\n")
print(pivot_table)

# Bar plot
fig, ax = plt.subplots(figsize=(12, 10))

ax.bar(
    pivot_table.index,
    pivot_table['sales'],
    color=['steelblue', 'coral', 'mediumseagreen'],
    edgecolor='black',
    width=0.5
)

ax.set_title('Total Sales Per Product', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Products', fontsize=14)
ax.set_ylabel('Total Sales ($)', fontsize=14)

# Add value labels on top of each bar
for i, (product, row) in enumerate(pivot_table.iterrows()):
    ax.text(i, row['sales'] + (pivot_table['sales'].max() * 0.01),
            f"${row['sales']:,.0f}", ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.savefig('total_sales_per_product_bar.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nBar chart saved as 'total_sales_per_product_bar.png'")