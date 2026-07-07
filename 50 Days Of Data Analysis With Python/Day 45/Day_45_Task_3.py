# For this challenge, you are going to preprocess and analyze
# the medical data of patients. The name of the file is
# medical_data , and it is in CSV format.

#3 You must have noticed that there are two columns with names.
#As part of feature engineering, you are required to create a copy of your DataFrame (question 1).
# Combine the "First Name" column and the "Last Name" column into one column called "Names."

import pandas as pd

# Load the dataset
df = pd.read_csv("medical_data.csv")

# Create a copy of the DataFrame
df_copy = df.copy()

# Combine First Name and Last Name into a new column
df_copy["Names"] = df_copy["First Name"] + " " + df_copy["Last Name"]

# Display the first 5 rows
print(df_copy.head())