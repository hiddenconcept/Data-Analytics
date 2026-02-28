#For this challenge, you are going to work with the data below.
# You are going to use NumPy functionality to answer questions using this data.
# This challenge will test your ability to use slicing to extract specific columns or rows of the data and perform operations on them.
# You will import a CSV file called names_age_sex_data.

#4.	Write another code snippet to return an array of all the males in the dataset. How many males are in the dataset?

import numpy as np

arr = np.genfromtxt('names_age_sex_data.csv',
                    delimiter=',',
                    dtype=str,
                    skip_header=1,)
print("\nOriginal Array:\n",arr)

arr_T = arr.T
print("\nTransposed  Array:\n",arr_T)

# Correct column order: Name, Sex, Age
names_col = arr_T[0]
sex_col = arr_T[1]
ages_col = arr_T[2]

mask = sex_col == 'Male'

male_names = names_col[mask]

print("\nHow many Males are in the datset by name :\n", male_names)

print("\nHow many Males are in the dataset by number:\n",len(male_names))





