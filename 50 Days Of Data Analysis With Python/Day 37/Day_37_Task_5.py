#Stock market data is typically time-series data, which means it('s collected and recorded over time.
#For this challenge, you are going to import the Fusion Systems fusion_stock_data dataset. This is a CSV file.

# 5 Calculate the daily returns of the stock price using pandas "pct_change" and plot a line plot using pandas.

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("fusion_stock_data.csv")

# Convert date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Set date as index
df = df.set_index("Date")

# Calculate daily returns (based on stock price column)
df["Daily_Return"] = df["Price"].pct_change()

# Plot daily returns
plt.figure(figsize=(10, 5))
df["Daily_Return"].plot()

# Labels and title
plt.xlabel("Date")
plt.ylabel("Daily Return")
plt.title("Fusion Systems Daily Stock Returns")

plt.show()