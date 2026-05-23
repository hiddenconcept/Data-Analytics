#Stock market data is typically time-series data, which means it('s collected and recorded over time.
#For this challenge, you are going to import the Fusion Systems fusion_stock_data dataset. This is a CSV file.

# 4What was the volume on the day with the lowest stock price?

import pandas as pd

# Load dataset
df = pd.read_csv("fusion_stock_data.csv")

# Convert date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Set date as index
df = df.set_index("Date")

# Find the row with the lowest stock price (usually "Close")
lowest_price_row = df["Price"].idxmin()

# Get the volume on that day
volume_on_lowest_day = df.loc[lowest_price_row, "Volume"]

print("\nDate with lowest stock price:", lowest_price_row)
print("Volume on lowest stock price day:", volume_on_lowest_day)

