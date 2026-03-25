#Using just pandas, find the least profitable product.

products = ["Sugar","Salt","Oil","Diapers","Rice"]
costs = [2450,1989,6745,9807,8743]
sales = [27908,4508,6743,9976,9000]

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

# Find least profitable product
least_profitable = df.loc[df['Profit'].idxmin()]
print(f"\nLeast Profitable Product: {least_profitable['Product']} with a profit of ${least_profitable['Profit']:,}")

# Highlight least profitable
colors = ['gold' if p == df['Profit'].min() else 'steelblue' for p in df['Profit']]

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