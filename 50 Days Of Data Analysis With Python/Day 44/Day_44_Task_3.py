#For this challenge, you are going to use the sports_data dataset.
#The file is a CSV file. Here is a sample of the dataset below:

#3 Using pandas convert all the columns with the "object" data type to the "categorical" data type.
#Create a new variable for the data frame after the conversation.
# Check the memory size of the resulting DataFrame using the df.memory_usage() method.
# Compare your results to the results in question 2. What conclusion can you draw?

import pandas as pd

# Load the dataset
df = pd.read_csv('sports_data.csv')

# Convert object columns to categorical
df_category = df.copy()

for column_name, column_data in df_category.items():
    if column_data.dtype == "object":
        df_category[column_name] = column_data.astype("category")

# Check memory usage of the new DataFrame
memory_usage_category = df_category.memory_usage(deep=True)
print(memory_usage_category)

# Calculate total memory usage in kilobytes
total_memory_kb_category = memory_usage_category.sum() / 1024
print(f"\nTotal memory usage after conversion: {total_memory_kb_category:.2f} KB")