#Learning .loc and .iloc attributes in pandas is important for data analysis because they provide a powerful and flexible
#way to select and manipulate data in a DataFrame. They are essential tools for any data analyst working with pandas.
#The challenges below require that you use these attributes in your analysis.
#You will continue to work with the retail_shop_data CSV file.

#1 Using .loc attribute, calculate the profit of the sunglasses.

import pandas as pd
import numpy as np

df1 = pd.read_csv('retail_shop_data.csv')

sunglasses_profit = df1.loc[df1['Product Name'] == 'Sunglasses', 'Price'].values[0] - \
                    df1.loc[df1['Product Name'] == 'Sunglasses', 'Cost'].values[0]

sunglasses_quantity = df1.loc[df1['Product Name'] == 'Sunglasses', 'Quantity'].values[0]
sunglasses_total_profit = sunglasses_profit * sunglasses_quantity

print("\nRetail Shop Data:\n", df1)
print("\nThe Sunglasses Profit:\n", sunglasses_profit)
print("\nSunglasses Total Profit(Total Profit = (Price - Cost) × Quantity):\n", sunglasses_total_profit)

