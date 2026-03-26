#Import the JSON file using pandas. View the last 5 rows of the DataFrame.

import pandas as pd

# Import JSON file
df = pd.read_json('data.json')

# View last 5 rows
print(df.tail(5))