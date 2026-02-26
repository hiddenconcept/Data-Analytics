import pandas as pd
import requests
import io

from openpyxl.utils.datetime import to_excel

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
tables = pd.read_html(io.StringIO(r.text))
df = tables[0:3]
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df)

df1 = tables[0]
df2 = tables[1]
df3 = tables[2]
df3.columns = [' '.join(col).strip() for col in df3.columns.values]

with pd.ExcelWriter('Largest Banks.xlsx', engine ='openpyxl') as writer:
    df1.to_excel(writer, sheet_name = 'Sheet1', index = False)
    df2.to_excel(writer,sheet_name = 'Sheet2', index = False)
    df3.to_excel(writer,sheet_name = 'Sheet3', index = False)

print("Your File as now been saved as a Spreadsheet!")