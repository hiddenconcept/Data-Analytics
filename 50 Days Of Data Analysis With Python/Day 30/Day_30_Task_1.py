#For this challenges, you are going to use the furniture_data CSV file. You will clean the data and create visualizations.

#1. Import the furniture_data CSV file using pandas. Check the length of the DataFrame.
#Find the sum of duplicates in the "Product" column.
# Using the pandas pivot_table() function, return a table that shows how many times each product appears in the "Product"
# column. This table will reveal which products are duplicated.

import pandas as pd

df = pd.read_csv('furniture_data.csv')
print("\nFurniture Store Data Table:\n",df.head())

#Chekcing the length
print("\nLength of Table:\n",len(df))

#Checking for duplicates
num_duplicates = df['Product'].duplicated().sum()
print(f"\nThere are: {num_duplicates} duplicate entries.")

#Pivot Table
pivot = df.pivot_table(index='Product', values='Sale Price', aggfunc='count')
pivot.columns = ['Count']
print("\nPivot Table:\n", pivot)