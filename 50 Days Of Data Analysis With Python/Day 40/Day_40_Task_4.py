#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts_expanded.csv dataset.

#4 Filter the DataFrame to return only columns with integer data types. Save this as a new variable.

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spare_parts.csv")

# Filter only integer columns
integer_columns = df.select_dtypes(include=['int64'])

print("Integer Columns:")
print(integer_columns)