#For this challenge, you are going to work with the data below.
# You are going to use NumPy functionality to answer questions using this data.
# This challenge will test your ability to use slicing to extract specific columns or rows of the data and perform operations on them.
# You will import a CSV file called names_age_sex_data.

#2.	Using NumPy, write code that returns all the names of people who are 56 years old.


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

mask = ages_int == 56

names_56 = names_col[mask]

print("\nNames of People over age of 56:\n", names_56)

if len(names_56) == 0:
    print("\nNo People with age of 56 found!\n")
else:
    print("\nPeople with age of 56 found:\n",names_56)



