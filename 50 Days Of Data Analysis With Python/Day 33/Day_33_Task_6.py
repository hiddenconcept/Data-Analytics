#6 Using pandas, group the data by "day_of_week" and "referral_source"
# columns and find the average of the visits and revenue for each group

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("website_data_analysis.csv")

# Define correct weekday order (used multiple times below)
day_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

# Average bounce by day of week
average_bounce = df.groupby("day_of_week")["bounce"].mean()
print("\nAverage Bounce by Day:\n", average_bounce)

# Average visits per website
average_visits = df.groupby("website")["visits"].mean()

# Create new column: visits per visitor
df["visits_per_visitor"] = df["visits"] / df["unique_visitors"]

# Top 5 websites by total visits
top_websites = (
    df.groupby("website")["visits"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Group by day_of_week and referral_source, calculate average visits and revenue
grouped_data = df.groupby(["day_of_week", "referral_source"]).agg({
    "visits": "mean",
    "revenue": "mean"
}).reset_index()

# Rename columns for clarity
grouped_data.columns = ["day_of_week", "referral_source", "unique_visitors", "revenue"]

# Apply correct day ordering
grouped_data["day_of_week"] = pd.Categorical(
    grouped_data["day_of_week"],
    categories=day_order,
    ordered=True
)

# Sort by day and referral source
grouped_data = grouped_data.sort_values(["day_of_week", "referral_source"])

print("\n" + "="*60)
print("Average Visits and Revenue by Day of Week and Referral Source")
print("="*60)
print(grouped_data)

# Optional: Save to CSV
grouped_data.to_csv("grouped_analysis.csv", index=False)
print("\n✓ Results saved to 'grouped_analysis.csv'")

print("\nDataFrame Preview:\n", df.head())