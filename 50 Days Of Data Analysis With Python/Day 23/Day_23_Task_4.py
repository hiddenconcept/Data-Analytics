#Using pandas, check for any duplicate values in the "Names" columns of your DataFrame (question 3).

import numpy as np
import pandas as pd


names = ["Kelly", np.nan, 'Jon', 'Ken', 'Tim', 'Pel']
grades = [30, 40, 30, 67, np.nan, 55]
age = [15, np.nan, 18, 17, np.nan, 16]


# Original DataFrame
df = pd.DataFrame({'names': names, 'grades': grades, 'age': age})

missing_percent = df.isnull().mean() * 100
cols_to_drop = missing_percent[missing_percent > 30].index
df_cleaned = df.drop(columns=cols_to_drop)

print("\nDataFrame (df_cleaned):\n",df_cleaned)


# --- Check for duplicates in the 'names' column ---
duplicate_names = df_cleaned['names'].duplicated()
print("\nDuplicate Check Per Row (True = duplicate):\n",duplicate_names)


print("\nNumber of Duplicate Names:\n", duplicate_names.sum())

print("\nDuplicated Name Values:\n")
print(df_cleaned[duplicate_names]['names'])