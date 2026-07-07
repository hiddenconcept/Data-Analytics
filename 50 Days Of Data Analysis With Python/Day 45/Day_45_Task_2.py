# For this challenge, you are going to preprocess and analyze
# the medical data of patients. The name of the file is
# medical_data , and it is in CSV format.

#2 What are the IQR ranges of the "BMI" column

import pandas as pd

# Load the dataset
df = pd.read_csv("medical_data.csv")

# Calculate Q1 and Q3
Q1 = df["BMI"].quantile(0.25)
Q3 = df["BMI"].quantile(0.75)

# Calculate the IQR
IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)