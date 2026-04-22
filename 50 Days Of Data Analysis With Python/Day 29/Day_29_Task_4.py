#For this challenge, you are going to analyze the data of a car service business.
# You will import the car_service_data CSV file.

#4 Using the pandas groupby() method, group the data by location and find the average profit margin per location.
#Format your output to 1 decimal place and present it as a percentage.

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


# Profit Margin (%) = ((Revenue - Cost) / Revenue) * 100
df['Profit Margin'] = ((df['Service Revenue'] - df['Service Cost']) / df['Service Revenue']) * 100

avg_profit_margin = (
    df.groupby('Location')['Profit Margin']
    .mean()
    .reset_index()
    .sort_values('Profit Margin', ascending=False)
)

# Format to 1 decimal place as percentage string
avg_profit_margin['Profit Margin (%)'] = avg_profit_margin['Profit Margin'].map('{:.1f}%'.format)

print("\n Average Profit Margin by Location:\n",
      avg_profit_margin[['Location', 'Profit Margin (%)']].to_string(index=False))
