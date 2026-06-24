#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts.csv dataset.

#7 The Seaborn pairplot is a very important tool for visualizing relationships between variables in a dataset.
#Use the pairplot to visualize the relationship of all the variables in the dataset (hue="spare_parts").

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("spare_parts.csv")

# Clean revenue column
df['total_revenue'] = (
    df['total_revenue']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

sns.pairplot(
    df,
    vars=['quantity', 'costs', 'sale_price', 'total_revenue'],
    hue='spare_part'
)

plt.show()