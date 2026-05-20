#You decided you don’t want to drop the missing numbers,but replace them with the mean of the numbers in the column.
#Create another copy of the DataFrame (from the original DataFrame in question 1) and fill in the missing values with the mean of the column.

import pandas as pd
import numpy as np

names = ["Carol", "Kate", "Jane", "Kuda", "Tito", "Kuku"]
age = [23, np.nan, 34, 56, np.nan, 44]

# Create the original DataFrame
df = pd.DataFrame({"names": names, "age": age})

# Create another copy of the original DataFrame
df_copy2 = df.copy()

# Fill missing values with the mean of the age column
df_copy2["age"] = df_copy2["age"].fillna(df_copy2["age"].mean())

print("Original:\n", df)
print("\nCopy with missing values replaced by mean:\n", df_copy2)
