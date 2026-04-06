#Import the retail_shop_data file and view the first 5 rows.
#Write another code to check how many rows and columns are in the DataFrame.
# Are there any duplicates?

import pandas as pd

#setup dataframe for csv
df = pd.read_csv('retail_shop_data.csv')
print("\nFirst 5 Rows:\n",df.head())

print("\nShape of DataFrame (rows,columns):\n",df.shape)

print("\nNumber of Duplicates Rows:\n",df.duplicated().sum())

print(df)