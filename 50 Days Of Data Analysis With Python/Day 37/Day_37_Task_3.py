#Stock market data is typically time-series data, which means it('s collected and recorded over time.
#For this challenge, you are going to import the Fusion Systems fusion_stock_data dataset. This is a CSV file.

#3 Using the pandas plot() method and Matplotlib, plot a line plot of the stock price over time.
#Ensure that your plot has axis labels and a title.

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("fusion_stock_data.csv")

# Convert date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Set date as index
df = df.set_index("Date")

# Plot stock price over time
plt.figure(figsize=(10, 5))
df["Volume"].plot()

# Labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Fusion Systems Stock Price Over Time")

# Show plot
plt.show()