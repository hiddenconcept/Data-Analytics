#Using the original DataFrame (question 1), write another code to set a hierarchical index, with the date column as the
#outer index and the products column as the inner index. Save this as a new variable.

import pandas as pd

# Import JSON file
df = pd.read_json('data.json')

# Convert date column to pandas datetime format
df['date'] = pd.to_datetime(df['date'])

# Set hierarchical index with date as outer and products as inner
df_hierarchical = df.set_index(['date', 'products'])

print(df_hierarchical)