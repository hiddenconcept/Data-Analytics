#Create a copy of the DataFrame in question 1 and drop all the missing values.

import pandas as pd
import numpy as np

names = ["Carol", "Kate", "Jane", "Kuda", "Tito", "Kuku"]
age = [23, np.nan, 34, 56, np.nan, 44]

# Create the original DataFrame first
df = pd.DataFrame({"names": names, "age": age})

# Create a copy of the DataFrame
df_copy = df.copy()

# Drop all missing values
df_copy = df_copy.dropna()

print("Original:\n", df)
print("\nCopy with no missing values:\n", df_copy)
