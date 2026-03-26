#Using pandas, create a copy of the DataFrame and convert the "date" column into a pandas datetime format. Set the date as the index of the DataFrame.
#The "date" column should not be deleted when it is set as an index.

import pandas as pd

# Import JSON file
df = pd.read_json('data.json')

# Create a copy of the DataFrame
df_copy = df.copy()

# Convert "date" column to pandas datetime format
df_copy['date'] = pd.to_datetime(df_copy['date'])

# Set "date" as index without dropping the column
df_copy.index = df_copy['date']

print(df_copy)