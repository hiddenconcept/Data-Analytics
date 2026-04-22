#For this challenge, you are going to analyze the data of a car service business.
# You will import the car_service_data CSV file.

#3 Which location has the highest number of customers?
#Using Matplotlib, plot a pie chart of the location and number of customers.
#Present the number of customers as percentages.
#Apply the explode parameter to the location with the highest number of customers. Add a shadow to your plot.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('car_service_data.csv')

# Preview the data
print("\n Preview Retail ShopDataset:\n",df.head())
print("\n Return all column names:\n",df.columns.tolist())
print("\n Check Data Types:\n",df.dtypes)
print("\n Overall Info For Retail ShopDataset:\n",df.info())

# Clean currency columns
currency_cols = ['Service Cost', 'Service Revenue', 'Number of Customers', 'Advertising Cost']
for col in currency_cols:
    df[col] = df[col].str.replace(r'[$,]', '', regex=True).astype(float)


customers_by_location = (
    df.groupby('Location')['Number of Customers']
    .sum()
    .reset_index()
    .sort_values('Number of Customers', ascending=False)
)

print("\n Number of Customers by Location:\n", customers_by_location)
print(f"\n Highest customer location: {customers_by_location.iloc[0]['Location']}"
      f"  →  {customers_by_location.iloc[0]['Number of Customers']:,.0f} customers")

# Explode the location with the highest number of customers
top_location = customers_by_location.iloc[0]['Location']
explode = [0.1 if loc == top_location else 0 for loc in customers_by_location['Location']]

pie_colors = ['#2196F3', '#90CAF9', '#BBDEFB']

fig, ax = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax.pie(
    customers_by_location['Number of Customers'],
    labels=customers_by_location['Location'],
    autopct='%1.1f%%',
    explode=explode,
    shadow=True,
    colors=pie_colors[:len(customers_by_location)],
    startangle=140,
    textprops={'fontsize': 13}
)

# Bold the percentage labels
for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_fontsize(13)

ax.set_title('Number of Customers by Location', fontsize=15, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('customers_by_location_pie.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n Pie chart saved.")