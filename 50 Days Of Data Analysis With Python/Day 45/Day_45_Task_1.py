# For this challenge, you are going to preprocess and analyze
# the medical data of patients. The name of the file is
# medical_data , and it is in CSV format.

#1 Import the medical_data dataset and view the first 5 rows.
#Use the info() method to get insights in the data.

import pandas as pd

# Load the dataset
df = pd.read_csv("medical_data.csv")

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()