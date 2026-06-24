#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts.csv dataset.

#9 Use a Seaborn lineplot to visualize the trend of total sales over time for all items.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spare_parts.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Clean total_revenue column
df['total_revenue'] = (
    df['total_revenue']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

# Group sales by date
sales_over_time = df.groupby('date')['total_revenue'].sum().reset_index()

# Sort dates
sales_over_time = sales_over_time.sort_values('date')

# Create lineplot
sns.lineplot(
    data=sales_over_time,
    x='date',
    y='total_revenue'
)

plt.title('Total Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')

plt.xticks(rotation=45)

plt.show()