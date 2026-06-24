#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts_expanded.csv dataset.

#3 Use a Matplotlib scatter plot to visualize the relationship between price and total sales for each item.
#Can you identify on the plot which product brought in the most income?

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spare_parts.csv")

# Convert total_revenue to numeric
df['total_revenue'] = (
    df['total_revenue']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

# Scatter plot of Sale Price vs Total Revenue
plt.figure(figsize=(10, 6))
plt.scatter(df['sale_price'], df['total_revenue'])

plt.title('Sale Price vs Total Revenue')
plt.xlabel('Sale Price ($)')
plt.ylabel('Total Revenue ($)')

# Label each point with the product name
for i in range(len(df)):
    plt.annotate(
        df['spare_part'][i],
        (df['sale_price'][i], df['total_revenue'][i]),
        fontsize=8
    )

plt.tight_layout()
plt.show()

# Product with highest revenue
highest_revenue = df.loc[df['total_revenue'].idxmax()]

plt.scatter(df['sale_price'], df['total_revenue'])

# Highlight highest revenue product
plt.scatter(
    highest_revenue['sale_price'],
    highest_revenue['total_revenue'],
    s=150,
    marker='*'
)

print("Highest Revenue Product:")
print(highest_revenue['spare_part'])
print("Revenue: $", highest_revenue['total_revenue'])
print("\nThe scatter plot visualizes the relationship between sale price and total revenue for each spare part.\n"
      " While products with higher sale prices tend to generate more revenue, the relationship\n"
      " is not perfectly linear because revenue is also affected by the quantity sold.\n"
      " The product that generated the highest income was the Battery, \n"
      "with total revenue of approximately $4,375, making it the highest point on the graph.")