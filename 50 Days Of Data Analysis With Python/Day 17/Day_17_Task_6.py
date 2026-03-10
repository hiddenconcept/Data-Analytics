#Creating and modifying DataFrame is an essential skill for data analysts because it allows them to efficiently clean,
#transform, analyze, and report on data. It is a foundational skill that is used in many data-related tasks and workflows.
#In the challenges below, you will create and modify DataFrames.


#Create a DataFrame using the data below:

#Write code to extract a subset of the DataFrame containing only male individuals.
# Write another code to retrieve the name and age of the oldest male from the modified DataFrame.

import pandas as pd

names = ["John", "Mary", "Peter"]
age = [27, 34, 47]
sex = ["Male", "Female", "Female"]

df = pd.DataFrame({"names": names, "age": age, "sex": sex})
print("\nOriginal DataFrame:\n", df)

# Access John's age using .loc
print("\nJohn's age:", df.loc[0, "age"])

# Change Peter's gender from "Female" to "Male" using .loc
df.loc[2, "sex"] = "Male"
print("\nUpdated DataFrame:\n", df)

# Extract subset containing only male individuals
males_df = df[df["sex"] == "Male"]
print("\nMale individuals only:\n", males_df)

# Retrieve the name and age of the oldest male
oldest_male = males_df.loc[males_df["age"].idxmax()]
print("\nOldest Male:")
print(f"  Name: {oldest_male['names']}")
print(f"  Age:  {oldest_male['age']}")