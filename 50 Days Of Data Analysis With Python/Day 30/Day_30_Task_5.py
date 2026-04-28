#For this challenges, you are going to use the furniture_data CSV file. You will clean the data and create visualizations.

#5 Which product has the least profit margin?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
df['Cost Per Product'] = pd.to_numeric(df['Cost Per Product'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df = df.dropna(subset=['Sale Price', 'Quantity', 'Cost Per Product'])
df['Total Revenue'] = df['Sale Price'] * df['Quantity']

# --- Task 4: Insert Total_Cost between Quantity and Total Revenue ---
total_cost = df['Cost Per Product'] * df['Quantity']
df.insert(4, 'Total_Cost', total_cost)

print("\nDataFrame with Total_Cost inserted:\n", df)

# --- Revenue Difference: Sofa vs Bed ---
sofa_revenue = df.loc[df['Product'] == 'Sofa', 'Total Revenue'].values[0]
bed_revenue  = df.loc[df['Product'] == 'Bed',  'Total Revenue'].values[0]
difference   = abs(sofa_revenue - bed_revenue)

print(f"\nSofa Revenue:  ${sofa_revenue:,.2f}")
print(f"Bed Revenue:   ${bed_revenue:,.2f}")
print(f"Difference:    ${difference:,.2f}")

# --- Task 5: Which product has the least profit margin? ---
df['Profit Margin (%)'] = ((df['Sale Price'] - df['Cost Per Product']) / df['Sale Price']) * 100

print("\nProfit Margins:\n", df[['Product', 'Sale Price', 'Cost Per Product', 'Profit Margin (%)']])

least_margin = df.loc[df['Profit Margin (%)'].idxmin()]
print(f"\nProduct with least profit margin: {least_margin['Product']}"
      f" ({least_margin['Profit Margin (%)']:.2f}%)")

# --- Profit Margin Chart ---
df_sorted = df.sort_values('Profit Margin (%)')
colors = ['#e74c3c' if p == df_sorted['Profit Margin (%)'].min() else '#3498db' for p in df_sorted['Profit Margin (%)']]

fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.barh(df_sorted['Product'], df_sorted['Profit Margin (%)'], color=colors, edgecolor='white', height=0.5)

for bar, val in zip(bars, df_sorted['Profit Margin (%)']):
    ax.text(val + 0.5, bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}%", va='center', ha='left', fontsize=13, fontweight='bold', color='#2c3e50')

ax.axvline(x=df['Profit Margin (%)'].mean(), color='gray', linestyle='--',
           linewidth=1.5, label=f"Avg: {df['Profit Margin (%)'].mean():.1f}%")

ax.set_xlabel('Profit Margin (%)', fontsize=12)
ax.set_title('Profit Margin by Product', fontsize=15, fontweight='bold', pad=15)
ax.set_xlim(0, 55)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

low_patch = mpatches.Patch(color='#e74c3c', label='Lowest margin')
high_patch = mpatches.Patch(color='#3498db', label='Other products')
ax.legend(handles=[low_patch, high_patch, ax.lines[0]], fontsize=10)

plt.tight_layout()
plt.savefig('profit_margin_chart.png', dpi=150)
plt.show()
print("\nPlot saved as 'profit_margin_chart.png'")