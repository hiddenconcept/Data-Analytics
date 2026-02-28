#For this challenge, you are going to work with the data below.
# You are going to use NumPy functionality to answer questions using this data.
# This challenge will test your ability to use slicing to extract specific columns or rows of the data and perform operations on them.
# You will import a CSV file called names_age_sex_data.

#5.	Calculate the average age of all the females in the table.
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

#boolean mask for females
mask = sex_col == 'Female'

#setting up the variable
female_age = ages_col[mask].astype(int)

#variable for avg
avg = np.mean(female_age)

print("\nFemale ages:\n",female_age)
print("\nAverage age of females:", avg)




