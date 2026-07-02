#For this challenge, you are going to explore the time series data.
#You will import the time_series_data CSV file. Here is a sample of the data below:

#3 Create a bar plot of the dataset, where the x-axis is the hour of the day (0–23)
# and the y-axis is the mean value for each hour.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("time_series_data.csv")

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Convert the value column to numeric
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Extract the hour from the date column
df["hour"] = df["date"].dt.hour

# Calculate the mean value for each hour
hourly_mean = df.groupby("hour")["value"].mean()

# Create the bar plot
plt.figure(figsize=(10, 5))
plt.bar(hourly_mean.index, hourly_mean.values)

# Add labels and title
plt.title("Mean Value by Hour of the Day")
plt.xlabel("Hour of the Day")
plt.ylabel("Mean Value")

# Show every hour (0-23) on the x-axis
plt.xticks(range(24))

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()