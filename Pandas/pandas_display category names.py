import pandas as pd

df = pd.read_excel('Asset_sales_data.xlsx')

# Check exact column names
print(df.columns.tolist())