# For this challenge, you are going to preprocess and analyze
# the medical data of patients. The name of the file is
# medical_data , and it is in CSV format.

#4 Now that you have combined the two columns,
# drop columns "First Name" and "Last Name"
# from the DataFrame and change the order of the columns to:
# [Name,First Letter, BMI, Gender, Condition] .

import pandas as pd

# Load the dataset
df = pd.read_csv("medical_data.csv")

# Create a copy of the DataFrame
df_copy = df.copy()

# Combine First Name and Last Name
df_copy["Names"] = df_copy["First Name"] + " " + df_copy["Last Name"]

# Drop the original name columns
df_copy.drop(columns=["First Name", "Last Name"], inplace=True)

# Reorder the columns
df_copy = df_copy[["Names", "First Letter", "BMI", "Gender", "Condition"]]

# Display the first 5 rows
print(df_copy.head())