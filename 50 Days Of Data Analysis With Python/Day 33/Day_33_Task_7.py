#7 Using pandas, calculate the revenue rate for each referral source and create a pie chart to visualize the breakdown of
# revenue rate by referral source. Which referral source brought it the most revenue?

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
grouped_data.columns = ["day_of_week", "referral_source", "avg_visits", "avg_revenue"]

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


# Calculate total revenue by referral source
revenue_by_source = df.groupby("referral_source")["revenue"].sum().sort_values(ascending=False)

# Calculate revenue rate (percentage of total revenue)
total_revenue = revenue_by_source.sum()
revenue_rate = (revenue_by_source / total_revenue) * 100

print("\n" + "="*60)
print("Revenue Rate by Referral Source")
print("="*60)
print(revenue_rate)
print(f"\nTotal Revenue: ${total_revenue:,.2f}")

# Identify the top revenue source
top_source = revenue_by_source.idxmax()
top_source_revenue = revenue_by_source.max()
top_source_percentage = revenue_rate.max()

print("\n" + "="*60)
print(f"🏆 Top Referral Source: {top_source}")
print(f"   Revenue: ${top_source_revenue:,.2f}")
print(f"   Percentage of Total: {top_source_percentage:.2f}%")
print("="*60)

# Create pie chart
plt.figure(figsize=(10, 8))

colors = plt.cm.Set3(range(len(revenue_by_source)))

plt.pie(
    revenue_by_source,
    labels=revenue_by_source.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=[0.1 if i == 0 else 0 for i in range(len(revenue_by_source))]  # Explode the largest slice
)

plt.title("Revenue Breakdown by Referral Source", fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.tight_layout()
plt.show()

