#For this challenge, you are going to work with the data below.
# You are going to use NumPy functionality to answer questions using this data.
# This challenge will test your ability to use slicing to extract specific columns or rows of the data and perform operations on them.
# You will import a CSV file called names_age_sex_data.

#1.	Your task is to import the CSV file using NumPy’s genfromtxt() function.

#A.	Transpose the array.

#B.	Using slicing, create three arrays: an array of all the names in the column, an array of the age column, and an array of the gender (sex) column.


import numpy as np

arr = np.genfromtxt('names_age_sex_data.csv',
                    delimiter=',',
                    dtype=str,
                    skip_header=1,)
print("\nOriginal Array:\n",arr)

arr_T = arr.T
print("\nTransposed  Array:\n",arr_T)

#First row
names_col = arr_T[0]
print("\nNames Array:\n",names_col)

#Second Row
ages_col = arr_T[1]
print("\nAges Array:\n",ages_col)

#Third Row
grades_col = arr_T[2]
print("\nGrades Array:\n",grades_col)
