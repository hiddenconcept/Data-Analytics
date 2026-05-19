#5 Using Seaborn, create a line plot to show the trend of unique visitors over time.
# Group the data by the day of the week.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("website_data_analysis.csv")

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

# Bar plot: Top websites
plt.figure(figsize=(10, 6))
top_websites.plot(kind="bar", color="skyblue")

plt.title("Top 5 Websites by Page Views")
plt.xlabel("Website")
plt.ylabel("Total Page Views")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Group by day of week (average unique visitors)
visitors_by_day = df.groupby("day_of_week")["unique_visitors"].mean().reset_index()

# Correct weekday order
day_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

visitors_by_day["day_of_week"] = pd.Categorical(
    visitors_by_day["day_of_week"],
    categories=day_order,
    ordered=True
)

visitors_by_day = visitors_by_day.sort_values("day_of_week")

# Line plot
plt.figure(figsize=(10, 5))

sns.lineplot(
    data=visitors_by_day,
    x="day_of_week",
    y="unique_visitors",
    marker="o"
)

plt.title("Trend of Unique Visitors by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Average Unique Visitors")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nDataFrame Preview:\n", df.head())
