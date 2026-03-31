#Using pandas import the Excel file above.
# Write a code to view the first 5 rows of your DataFrame.

import pandas as pd

df = pd.read_excel('Asset_sales_data.xlsx')

# View the first 5 rows
print("\nFirst 5 rows:\n",df.head())