#Update your DataFrame (question 3) with the gender column using the gender_values list above.
# Use the melt() method to reshape the DataFrame and create a new DataFrame with two columns: the "names" column and the
#"gender" and "age" columns combined.
#This will change the DataFrame from a wide format to a long format.

import pandas as pd
import numpy as np

names = ["Carol", "Kate", "Jane", "Kuda", "Tito", "Kuku"]
age = [23, np.nan, 34, 56, np.nan, 44]
gender_values = ["F", "F", "F", "M", "M", "M"]

# Create the original DataFrame
df = pd.DataFrame({"names": names, "age": age})

# Create another copy of the original DataFrame
df_copy2 = df.copy()

# Fill missing values with the mean of the age column
df_copy2["age"] = df_copy2["age"].fillna(df_copy2["age"].mean())

# Add the gender column to df_copy2
df_copy2["gender"] = gender_values

print("Updated DataFrame with gender column:\n", df_copy2)

# Use melt() to reshape from wide to long format
df_melted = df_copy2.melt(id_vars="names", value_vars=["age", "gender"],
                           var_name="variable", value_name="value")

print("\nMelted DataFrame (long format):\n", df_melted)