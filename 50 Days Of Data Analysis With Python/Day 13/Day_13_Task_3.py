#In this challenge:
#your objective is to demonstrate your proficiency in creating arrays from lists and extracting specific information from those arrays.
#You have the following data:
names = ["John","Kelly","Jos","Peter","Robert","Piper"]
age = [21,21,56,44,56,96]
gender =[ 'M','F','M','M','M','F']

#3.	Using slicing or indexing, write code to return the first two rows of the transposed array (question 1).

import numpy as np

arr = np.array([names,age,gender]).T
print("\n Array:\n", arr)



print()
print("\nFirst Two Rows Of The Array:\n", arr[0:2])



