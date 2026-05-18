#2 Add another column to the DataFrame that calculates the number of website visits per unique visitor.

import pandas as pd

# Load the dataset
df = pd.read_csv("website_data_analysis.csv")

# Find the average number of visits per website
average_visits = df.groupby("website")["visits"].mean()

# Create a new column
df["visits_per_visitor"] = df["visits"] / df["unique_visitors"]

# Display the updated DataFrame
print("\nDataFrame:\n",df.head())

