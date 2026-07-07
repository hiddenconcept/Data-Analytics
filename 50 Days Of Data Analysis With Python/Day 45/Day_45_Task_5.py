# For this challenge, you are going to preprocess and analyze
# the medical data of patients. The name of the file is
# medical_data , and it is in CSV format.

#5 The "Gender" column is combined with the age.
# Your task is to create a new column for age by separating age from the "Gender" column.
# Once you do that, make the condition column the last column of the DataFrame.
# Your columns' order must be: [Name, First Letter, BMI, Gender, Age, Condition].

import pandas as pd

# Load the dataset
df = pd.read_csv("medical_data.csv")

# Create a copy of the DataFrame
df_copy = df.copy()

# Combine First Name and Last Name
df_copy["Name"] = df_copy["First Name"] + " " + df_copy["Last Name"]

# Drop original name columns
df_copy.drop(columns=["First Name", "Last Name"], inplace=True)

# Extract Gender (letters only)
df_copy["Gender"] = df_copy["Gender"].str.extract(r"([A-Za-z]+)")

# Extract Age (numbers only)
df_copy["Age"] = df["Gender"].str.extract(r"(\d+)").astype(int)

# Reorder columns
df_copy = df_copy[["Name", "First Letter", "BMI", "Gender", "Age", "Condition"]]

# Display the first 5 rows
print(df_copy.head())