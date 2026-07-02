#For this challenge, you are going to explore the time series data.
#You will import the time_series_data CSV file. Here is a sample of the data below:

#2 Create a line plot of the dataset, where the x-axis is the date and time and the y-axis is the value.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("time_series_data.csv")

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Convert the value column to numeric
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Create the line plot
plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["value"])

# Add labels and title
plt.title("Time Series Data")
plt.xlabel("Date and Time")
plt.ylabel("Value")

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()