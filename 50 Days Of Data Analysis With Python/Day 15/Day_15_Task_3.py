#For this challenge, you are going to work with the data below.
# You are going to use NumPy functionality to answer questions using this data.
# This challenge will test your ability to use slicing to extract specific columns or rows of the data and perform operations on them.
# You will import a CSV file called names_age_sex_data.

#3.	How many people are aged 44 or under?

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

ages_int = ages_col.astype(int)

mask = ages_int <= 44

names_44 = names_col[mask]

print("\nNames of People over age of 44 and under:\n", names_44)
print("\nTotal count:", len(names_44))





