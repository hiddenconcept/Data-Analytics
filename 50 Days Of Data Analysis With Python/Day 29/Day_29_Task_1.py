#For this challenge, you are going to analyze the data of a car service business.
# You will import the car_service_data CSV file.

#1 Import the car_service_data CSV file. Write a code to return all the column names in the DataFrame.
#Check the data types of the DataFrame.

import pandas as pd

df = pd.read_csv('car_service_data.csv')

# Preview the data
print("\n Preview Retail ShopDataset:\n",df.head())

# Return all column names
print("\n Return all column names:\n",df.columns.tolist())

# Check data types
print("\n Check Data Types:\n",df.dtypes)

# Bonus: overall info (combines shape, columns, dtypes, and null counts)
print("\n Overall Info For Retail ShopDataset:\n",df.info())

