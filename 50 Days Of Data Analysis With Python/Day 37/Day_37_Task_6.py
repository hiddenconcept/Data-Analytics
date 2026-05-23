#Stock market data is typically time-series data, which means it('s collected and recorded over time.
#For this challenge, you are going to import the Fusion Systems fusion_stock_data dataset. This is a CSV file.

# 6 What date had the highest price?

import pandas as pd

# Load dataset
df = pd.read_csv("fusion_stock_data.csv")

# Convert date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Set date as index
df = df.set_index("Date")

# Find the date with the highest price
highest_price_date = df["Price"].idxmax()
highest_price_value = df["Price"].max()

print("\nDate with highest stock price:")
print(highest_price_date)

print("\nHighest stock price value:")
print(highest_price_value)