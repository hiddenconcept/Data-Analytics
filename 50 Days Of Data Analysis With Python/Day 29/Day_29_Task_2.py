#For this challenge, you are going to analyze the data of a car service business.
# You will import the car_service_data CSV file.

#2 Which location has the highest service costs? Plot a bar plot using Seaborn to visualize the service costs by location.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('car_service_data.csv')

# Preview the data
print("\n Preview Retail ShopDataset:\n",df.head())
print("\n Return all column names:\n",df.columns.tolist())
print("\n Check Data Types:\n",df.dtypes)
print("\n Overall Info For Retail ShopDataset:\n",df.info())

currency_cols = ['Service Cost', 'Service Revenue', 'Number of Customers', 'Advertising Cost']
for col in currency_cols:
    df[col] = df[col].str.replace(r'[$,]', '', regex=True).astype(float)


cost_by_location = (
    df.groupby('Location')['Service Cost']
    .sum()
    .reset_index()
    .sort_values('Service Cost', ascending=False)
)

print("\n Service Costs by Location:\n", cost_by_location)
print(f"\n Highest cost location: {cost_by_location.iloc[0]['Location']}"
      f"  →  ${cost_by_location.iloc[0]['Service Cost']:,.2f}")

# ── Bar Plot ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6))

colors = ['#2196F3' if i == 0 else '#90CAF9' for i in range(len(cost_by_location))]

sns.barplot(
    data=cost_by_location,
    x='Location',
    y='Service Cost',
    hue='Location',
    palette=dict(zip(cost_by_location['Location'], colors)),
    order=cost_by_location['Location'],
    legend=False,
    ax=ax
)

# Annotate bars
for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 10,
        f"${bar.get_height():,.0f}",
        ha='center', va='bottom',
        fontsize=12, fontweight='bold', color='#333333'
    )

ax.set_title('Total Service Costs by Location', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Location', fontsize=12)
ax.set_ylabel('Total Service Cost ($)', fontsize=12)
ax.set_ylim(0, cost_by_location['Service Cost'].max() * 1.2)
sns.despine()

plt.tight_layout()
plt.savefig('service_costs_by_location.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n Plot saved.")


