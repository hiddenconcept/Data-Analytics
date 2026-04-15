#Learning .loc and .iloc attributes in pandas is important for data analysis because they provide a powerful and flexible
#way to select and manipulate data in a DataFrame. They are essential tools for any data analyst working with pandas.
#The challenges below require that you use these attributes in your analysis.
#You will continue to work with the retail_shop_data CSV file.

#2 Using .loc attribute, calculate the profit of hoodies.

import pandas as pd
import numpy as np

df1 = pd.read_csv('retail_shop_data.csv')

hoodie_profit = df1.loc[df1['Product Name'] == 'Hoodie', 'Price'].values[0] - \
                    df1.loc[df1['Product Name'] == 'Hoodie', 'Cost'].values[0]

hoodie_quantity = df1.loc[df1['Product Name'] == 'Hoodie', 'Quantity'].values[0]
hoodie_total_profit = hoodie_profit * hoodie_quantity

print("\nRetail Shop Data:\n", df1)
print("\nThe Hoodie Profit:\n", hoodie_profit)
print("\nHoodie Total Profit(Total Profit = (Price - Cost) × Quantity):\n", hoodie_total_profit)

