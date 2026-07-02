#For this challenge, you are going to explore the time series data.
#You will import the time_series_data CSV file. Here is a sample of the data below:

#1 Resample the dataset at daily intervals and calculate the maximum value for each day.

import pandas as pd

# Load the dataset
df = pd.read_csv("time_series_data.csv")

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Convert the value column to numeric, invalid values become NaN
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Set the date column as the index
df.set_index("date", inplace=True)

# Resample by day and calculate the maximum value for each day
daily_max = df.resample("D")["value"].max()

# Display the result
print(daily_max)