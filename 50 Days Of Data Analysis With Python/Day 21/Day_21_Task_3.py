#Using Matplotlib, create a line trend plot of sales and date.

import pandas as pd
import matplotlib.pyplot as plt

# Import JSON file
df = pd.read_json('data.json')

# Create a copy of the DataFrame
df_copy = df.copy()

# Convert "date" column to pandas datetime format
df_copy['date'] = pd.to_datetime(df_copy['date'])

# Set "date" as index without dropping the column
df_copy.index = df_copy['date']

# Line trend plot of sales and date
plt.figure(figsize=(12, 6))
plt.plot(df_copy['date'], df_copy['sales'], marker='o', color='steelblue', linewidth=2, label='Sales')

plt.title('Sales Trend Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=13)
plt.ylabel('Sales ($)', fontsize=13)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('sales_trend.png', dpi=150)
plt.show()