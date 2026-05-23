#Stock market data is typically time-series data, which means it('s collected and recorded over time.
#For this challenge, you are going to import the Fusion Systems fusion_stock_data dataset. This is a CSV file.

#2 Convert the date column into datetime format and set it as the index.

import pandas as pd

# Load dataset
df = pd.read_csv("fusion_stock_data.csv")

# Convert date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Set date as index
df = df.set_index("Date")

print("\nData after setting Date as index:")
print(df.head())

# Optional: verify index type
print("\nIndex type:")
print(df.index)