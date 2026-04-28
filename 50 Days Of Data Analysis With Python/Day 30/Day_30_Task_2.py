#For this challenges, you are going to use the furniture_data CSV file. You will clean the data and create visualizations.

#2. Use Seaborn regplot() to fit a linear regression model and visualize the relationship between the price of each item
#and total revenue.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('furniture_data.csv')
print("\nFurniture Store Data Table:\n", df.head())

# Checking the length
print("\nLength of Table:\n", len(df))

# Checking for duplicates
num_duplicates = df['Product'].duplicated().sum()
print(f"\nThere are: {num_duplicates} duplicate entries.")

# Pivot Table
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

# --- Seaborn regplot: Price vs Total Revenue ---
plt.figure(figsize=(9, 6))

sns.regplot(
    data=df,
    x='Sale Price',
    y='Total Revenue',
    scatter_kws={'alpha': 0.6, 'color': 'steelblue', 's': 80},
    line_kws={'color': 'red', 'linewidth': 2}
)

plt.title('Sale Price vs Total Revenue (Linear Regression)', fontsize=14)
plt.xlabel('Sale Price ($)', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.tight_layout()
plt.savefig('price_vs_revenue_regplot.png', dpi=150)
plt.show()
print("\nPlot saved as 'price_vs_revenue_regplot.png'")