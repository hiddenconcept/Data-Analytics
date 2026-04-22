#For this challenge, you are going to analyze the data of a car service business.
# You will import the car_service_data CSV file.

#5  What is the advertising cost of each region as a percentage of total revenue?
# Using the rank() method, rank each region by the cost of advertising as a percentage of revenue
#in descending order (add a rank column to the grouped data).
# Which region has the lowest rank?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('car_service_data.csv')

# Preview the data
print("\n Preview Retail ShopDataset:\n",df.head())
print("\n Return all column names:\n",df.columns.tolist())
print("\n Check Data Types:\n",df.dtypes)
print("\n Overall Info For Retail ShopDataset:\n",df.info())

# Preview the data
print("\n Preview Car Service Dataset:\n", df.head())
print("\n Return all column names:\n", df.columns.tolist())
print("\n Check Data Types:\n", df.dtypes)
print("\n Overall Info For Car Service Dataset:\n")
df.info()

# Clean currency columns
currency_cols = ['Service Cost', 'Service Revenue', 'Number of Customers', 'Advertising Cost']
for col in currency_cols:
    df[col] = df[col].str.replace(r'[$,]', '', regex=True).astype(float)

grouped = (
    df.groupby('Location')[['Advertising Cost', 'Service Revenue']]
    .sum()
    .reset_index()
)

# Advertising cost as a percentage of total revenue
grouped['Ad Cost % of Revenue'] = (grouped['Advertising Cost'] / grouped['Service Revenue']) * 100

# Rank in descending order (highest % = rank 1)
grouped['Rank'] = grouped['Ad Cost % of Revenue'].rank(ascending=False).astype(int)

# Sort by rank and format output
grouped = grouped.sort_values('Rank')
grouped['Ad Cost % of Revenue'] = grouped['Ad Cost % of Revenue'].map('{:.1f}%'.format)

print("\n Advertising Cost as % of Revenue by Region:\n",
      grouped[['Rank', 'Location', 'Ad Cost % of Revenue']].to_string(index=False))

lowest_rank = grouped[grouped['Rank'] == grouped['Rank'].max()]
print(f"\n Region with the lowest rank: {lowest_rank.iloc[0]['Location']}"
      f"  →  Rank {lowest_rank.iloc[0]['Rank']}  ({lowest_rank.iloc[0]['Ad Cost % of Revenue']} ad cost/revenue)")

