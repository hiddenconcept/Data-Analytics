#For this challenge, you are going to use the sports_data dataset.
#The file is a CSV file. Here is a sample of the dataset below:

#2 Using a pandas method, check the memory size of each column using the df.memory_usage() method.
#Set the deep parameter to True.
#What is the total memory usage of theDataFrame in kilobytes?

import pandas as pd

# Load the dataset
df = pd.read_csv('sports_data.csv')

# Check memory usage of each column
memory_usage = df.memory_usage(deep=True)
print(memory_usage)

# Calculate total memory usage in kilobytes
total_memory_kb = memory_usage.sum() / 1024
print(f"\nTotal memory usage: {total_memory_kb:.2f} KB")