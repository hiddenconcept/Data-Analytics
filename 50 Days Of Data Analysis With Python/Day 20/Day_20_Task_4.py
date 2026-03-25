#Using pandas and Matplotlib, create a line plot of the costs and profits of all products.

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

# Line plot of costs and profits
plt.figure(figsize=(10, 6))
plt.plot(df['Product'], df['Cost'], marker='o', color='tomato', linewidth=2, label='Cost')
plt.plot(df['Product'], df['Profit'], marker='o', color='steelblue', linewidth=2, label='Profit')

plt.title('Cost vs Profit by Product', fontsize=16, fontweight='bold')
plt.xlabel('Product', fontsize=13)
plt.ylabel('Amount ($)', fontsize=13)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Add value labels
for i, (cost, profit) in enumerate(zip(df['Cost'], df['Profit'])):
    plt.text(i, cost + 200, f'${cost:,}', ha='center', fontsize=9, color='tomato')
    plt.text(i, profit + 200, f'${profit:,}', ha='center', fontsize=9, color='steelblue')

plt.tight_layout()
plt.savefig('cost_vs_profit_line.png', dpi=150)
plt.show()