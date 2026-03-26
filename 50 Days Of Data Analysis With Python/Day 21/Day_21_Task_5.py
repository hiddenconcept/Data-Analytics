#One of the benefits of setting a multiindex is that it makes it easy to filter data. Using the hierarchical index
# you set in question 4, calculate the profit of "Houses" on December 12, 2021.

import pandas as pd

# Import JSON file
df = pd.read_json('data.json')

# Convert date column to pandas datetime format
df['date'] = pd.to_datetime(df['date'])

# Set hierarchical index with date as outer and products as inner
df_hierarchical = df.set_index(['date', 'products'])

# Calculate profit column
df_hierarchical['profit'] = df_hierarchical['sales'] - df_hierarchical['cost']

# Filter for "Houses" on December 12, 2021
houses_profit = df_hierarchical.loc[('2021-12-12', 'Houses'), 'profit']

print(f"Profit of Houses on December 12, 2021: ${houses_profit:,}")