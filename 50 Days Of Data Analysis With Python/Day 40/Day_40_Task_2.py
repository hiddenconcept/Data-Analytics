#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts_expanded.csv dataset.

#2 Box plots are useful for identifying outliers, visualizing the median, quartiles,
# and range of the dataset, and comparing the distributions of different groups or categories within the dataset.
#Use a box plot of the Seaborn library to compare the distribution of total revenue for each product.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("spare_parts.csv")

# Convert total_revenue to numeric
df['total_revenue'] = (
    df['total_revenue']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

# Create box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='spare_part', y='total_revenue', data=df)

plt.title('Distribution of Total Revenue by Spare Part')
plt.xlabel('Spare Part')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Histogram of total revenue
plt.figure(figsize=(8,5))
plt.hist(df['total_revenue'], bins=20)
plt.title("Distribution of Total Sales Revenue")
plt.xlabel("Revenue ($)")
plt.ylabel("Frequency")
plt.show()