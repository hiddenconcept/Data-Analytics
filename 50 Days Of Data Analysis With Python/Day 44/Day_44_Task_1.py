#For this challenge, you are going to use the sports_data dataset.
#The file is a CSV file. Here is a sample of the dataset below:

#1 Import the sports dataset and write code to check the first five rows to confirm that it has loaded (properly.
#Now, using the pandas items() method, return all the names of the columns that have values of the "object" data type.

import pandas as pd

# Load the dataset
df = pd.read_csv('sports_data.csv')

# Display the first five rows
print(df.head())

# Return the names of columns with the "object" data type
for column_name, column_data in df.items():
    if column_data.dtype == "object":
        print(column_name)