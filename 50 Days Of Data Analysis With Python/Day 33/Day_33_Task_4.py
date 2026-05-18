#4 Using pandas, group the data by day of the week and find the average bounce rate for each day.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("website_data_analysis.csv")

# Group by day of the week and find average bounce rate
average_bounce_rate = df.groupby("day_of_week")["bounce"].mean()

# Display results
print("\nAverage Bounce Rate by Day:\n")
print(average_bounce_rate)

# Find the average number of visits per website
average_visits = df.groupby("website")["visits"].mean()

# Create a new column
df["visits_per_visitor"] = df["visits"] / df["unique_visitors"]

# Find total page views per website
top_websites = (
    df.groupby("website")["visits"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Create the bar plot
plt.figure(figsize=(10, 6))
top_websites.plot(kind="bar", color="skyblue")

# Add titles and labels
plt.title("Top 5 Websites by Page Views")
plt.xlabel("Website")
plt.ylabel("Total Page Views")
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()

# Display the updated DataFrame
print("\nDataFrame:\n",df.head())

