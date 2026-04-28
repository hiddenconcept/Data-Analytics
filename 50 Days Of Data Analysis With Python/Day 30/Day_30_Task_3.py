#For this challenges, you are going to use the furniture_data CSV file. You will clean the data and create visualizations.

#3 What is the difference in revenue between "wardrobes" and "beds"?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('furniture_data.csv')
print("\nFurniture Store Data Table:\n", df.head())

print("\nLength of Table:\n", len(df))

num_duplicates = df['Product'].duplicated().sum()
print(f"\nThere are: {num_duplicates} duplicate entries.")

pivot = df.pivot_table(index='Product', values='Sale Price', aggfunc='count')
pivot.columns = ['Count']
print("\nPivot Table:\n", pivot)

# --- Data Cleaning ---
df = df.drop_duplicates(subset='Product', keep='first')
df['Sale Price'] = pd.to_numeric(df['Sale Price'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df = df.dropna(subset=['Sale Price', 'Quantity'])
df['Total Revenue'] = df['Sale Price'] * df['Quantity']

print("\nCleaned Data with Total Revenue:\n", df[['Product', 'Sale Price', 'Quantity', 'Total Revenue']])

# --- Revenue Difference: Sofa vs Bed ---
# (No 'Wardrobe' in dataset — using Sofa as the comparison item)
sofa_revenue = df.loc[df['Product'] == 'Sofa', 'Total Revenue'].values[0]
bed_revenue  = df.loc[df['Product'] == 'Bed',  'Total Revenue'].values[0]
difference   = abs(sofa_revenue - bed_revenue)

print(f"\nSofa Revenue:  ${sofa_revenue:,.2f}")
print(f"Bed Revenue:   ${bed_revenue:,.2f}")
print(f"Difference:    ${difference:,.2f}")

# --- Bar Chart Comparison ---
compare_df = df[df['Product'].isin(['Sofa', 'Bed'])].copy()

plt.figure(figsize=(7, 5))
ax = sns.barplot(data=compare_df, x='Product', y='Total Revenue',
                 hue='Product', palette=['steelblue', 'salmon'], legend=False)

for bar, val in zip(ax.patches, compare_df['Total Revenue']):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 300,
            f"${val:,.0f}",
            ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.title('Revenue Comparison: Sofa vs Bed', fontsize=14)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.tight_layout()
plt.savefig('revenue_comparison.png', dpi=150)
plt.show()
print("\nPlot saved as 'revenue_comparison.png'")