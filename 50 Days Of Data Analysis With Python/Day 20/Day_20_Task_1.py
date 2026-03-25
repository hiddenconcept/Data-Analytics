products = ["Sugar","Salt","Oil","Diapers","Rice"]
costs = [2450,1989,6745,9807,8743]
sales = [27908,4508,6743,9976,9000]

#Create a pandas DataFrame from the lists above. Find the most profitable product.
# Using Matplotlib, create a bar plot to visualize product profitability.

import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
df = pd.DataFrame({
    'Product': products,
    'Cost': costs,
    'Sales': sales
})

# Calculate profitability
df['Profit'] = df['Sales'] - df['Cost']

print("\nDataFrame with Profit:\n", df)

# Find most profitable product
most_profitable = df.loc[df['Profit'].idxmax()]
print(f"\nMost Profitable Product: {most_profitable['Product']} with a profit of ${most_profitable['Profit']:,}")

# Bar plot
colors = ['gold' if p == df['Profit'].max() else 'steelblue' for p in df['Profit']]

plt.figure(figsize=(10, 6))
plt.bar(df['Product'], df['Profit'], color=colors, edgecolor='black')

plt.title('Product Profitability', fontsize=16, fontweight='bold')
plt.xlabel('Product', fontsize=13)
plt.ylabel('Profit ($)', fontsize=13)

# Add value labels on top of each bar
for i, value in enumerate(df['Profit']):
    plt.text(i, value + 100, f'${value:,}', ha='center', fontsize=11)

plt.tight_layout()
plt.savefig('product_profitability.png', dpi=150)
plt.show()