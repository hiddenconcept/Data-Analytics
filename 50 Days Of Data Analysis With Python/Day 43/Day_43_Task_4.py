#For this challenge, you are going to explore the time series data.
#You will import the time_series_data CSV file. Here is a sample of the data below:

#4 The rolling average is a widely used statistical tool that smooths out short-term fluctuations in data and shows the longer-term trend of the data.
# Calculate the rolling average of the dataset using a window size of 3, and plot the original values and the rolling average on the same plot.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("time_series_data.csv")

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Convert the value column to numeric
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Calculate the rolling average with a window size of 3
df["rolling_average"] = df["value"].rolling(window=3).mean()

# Create the plot
plt.figure(figsize=(10, 5))

# Plot the original values
plt.plot(df["date"], df["value"], label="Original Values")

# Plot the rolling average
plt.plot(df["date"], df["rolling_average"], label="Rolling Average (Window = 3)")

# Add labels and title
plt.title("Original Values and Rolling Average")
plt.xlabel("Date and Time")
plt.ylabel("Value")

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Add a legend
plt.legend()

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()