#Stock market data is typically time-series data, which means it('s collected and recorded over time.
#For this challenge, you are going to import the Fusion Systems fusion_stock_data dataset. This is a CSV file.

#1 Load the dataset. Write a code to check the data types of the columns in the dataset.
#Check the data for any missing values using the isnull() method.

import pandas as pd

# Load dataset
df = pd.read_csv("fusion_stock_data.csv")

# Check data types of each column
print("\nData Types:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values (True = missing):")
print(df.isnull())