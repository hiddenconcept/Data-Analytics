# Use the apply() method to apply a thousand separators to the "sales" and "cost" columns (DataFrame from question 4).

# Use apply() to add thousand separators to "sales" and "cost" columns.

import pandas as pd

# Import JSON file
df = pd.read_json('data.json')

# Convert date column to pandas datetime format
df['date'] = pd.to_datetime(df['date'])

# Set hierarchical index with date as outer and products as inner
df_hierarchical = df.set_index(['date', 'products'])

# Apply thousand separators to sales and cost columns
df_hierarchical[['sales', 'cost']] = df_hierarchical[['sales', 'cost']].apply(
    lambda x: x.map(lambda v: f'{v:,}')
)

print(df_hierarchical)