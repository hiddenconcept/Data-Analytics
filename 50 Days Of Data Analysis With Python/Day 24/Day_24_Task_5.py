#Using Matplotlib, create a pie chart of the products and their sales values as percentages.
#Your chart should have labels and a title. Add explode (0, 0.1, 0) and a shadow.

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

# Group by product and sum sales
product_sales = df.groupby('products')['sales'].sum()

# Pie chart values and labels
labels = product_sales.index
values = product_sales.values
explode = (0, 0.1, 0)  # explode the 2nd slice

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    values,
    labels=labels,
    explode=explode,
    autopct='%1.1f%%',  # show percentage on each slice
    shadow=True,
    startangle=90  # start from top
)

ax.set_title('Product Sales Distribution (%)', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('product_sales_pie_chart.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nPie chart saved as 'product_sales_pie_chart.png'")