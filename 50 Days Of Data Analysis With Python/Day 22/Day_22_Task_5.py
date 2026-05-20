#Using the pandas where() method, write a code to return a DataFrame of names and gender values only from the
#"melted" DataFrame (question 4). Your DataFrame should not have NaN values. Save this to the new variable.

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

# Melt the DataFrame
df_melted = df_copy2.melt(id_vars="names", value_vars=["age", "gender"],
                           var_name="variable", value_name="value")

# Use where() to keep only rows where variable is "gender"
df_gender = df_melted.where(df_melted["variable"] == "gender").dropna()

# Keep only the names and value columns and rename value to gender
df_gender = df_gender[["names", "value"]].rename(columns={"value": "gender"})

# Reset the index
df_gender = df_gender.reset_index(drop=True)

print("Names and Gender DataFrame:\n", df_gender)