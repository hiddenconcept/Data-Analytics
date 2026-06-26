#In this challenge, you are going to gain insights and preprocess fictitious population data.
#You will import the population_data file, which is saved in CSV format.

#1 Import the dataset using pandas. View the first 5 columns.
#What is the data type of each column in the dataset? What is the shape of the DataFrame?

import pandas as pd

df = pd.read_csv('population_data.csv')

print("\nDataset:\n",df.head())
print("\nDataShape:",df.shape)
print("\nData Types:\n",df.dtypes)