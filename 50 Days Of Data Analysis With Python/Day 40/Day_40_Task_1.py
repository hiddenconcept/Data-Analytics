#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts_expanded.csv dataset.

#1.Load the CSV dataset above. Check the "date" and "revenue" data types.
#Write another code to check for any duplicates in the "spare_parts" column.
#Use a histogram to visualize the distribution of total sales for the entire store.
#Do you notice any outliers in the histogram?

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spare_parts.csv")

# Check data types
print("Original Data Types:")
print(df[['date', 'total_revenue']].dtypes)

# Convert total_revenue to numeric
df['total_revenue'] = (
    df['total_revenue']
    .replace({'\$': '', ',': ''}, regex=True)
    .astype(float)
)

# Check for duplicates in spare_part column
duplicate_count = df['spare_part'].duplicated().sum()

print("\nNumber of duplicate spare parts:", duplicate_count)

# Display duplicate entries
duplicates = df[df['spare_part'].duplicated()]
print("\nDuplicate spare parts:")
print(duplicates)

# Histogram of total revenue
plt.figure(figsize=(8,5))
plt.hist(df['total_revenue'], bins=20)
plt.title("Distribution of Total Sales Revenue")
plt.xlabel("Revenue ($)")
plt.ylabel("Frequency")
plt.show()