#Write another code that will return the data types of all the columns in the DataFrame.

import pandas as pd

df = pd.read_excel('Asset_sales_data.xlsx')

# View the first 5 rows
print("\nFirst 5 rows:\n",df.head())

#Return the data types
print("\nData Types of All Columns:\n",df.dtypes)
