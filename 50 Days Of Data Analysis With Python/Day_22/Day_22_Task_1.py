#Using pandas create a DataFrame with the two lists above.
#Write a code that counts how many missing values are in each column.

import pandas as pd
import numpy as np

names = ["Carol", "Kate", "Jane", "Kuda", "Tito", "Kuku"]
age = [23, np.nan, 34, 56, np.nan, 44]

# Create DataFrame
df = pd.DataFrame({"names": names, "age": age})

# Count missing values in each column
print(df.isnull().sum())