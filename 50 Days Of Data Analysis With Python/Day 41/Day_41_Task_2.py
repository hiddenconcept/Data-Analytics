#In this challenge, you are going to gain insights and preprocess fictitious population data.
#You will import the population_data file, which is saved in CSV format.

#2 Are there any missing values in the dataset? If so, how many and in which columns?

import pandas as pd

df = pd.read_csv('population_data.csv')

missing_values = df.isnull().sum()

print("\nMissing Values by Column:\n",missing_values)