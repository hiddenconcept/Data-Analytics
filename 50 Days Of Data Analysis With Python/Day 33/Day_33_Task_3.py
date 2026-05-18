#3 Using Matplotlib, create a bar plot to visualize the top 5 websites with the highest number of page views.
# The data plotted must be sorted in descending order.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("website_data_analysis.csv")

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

