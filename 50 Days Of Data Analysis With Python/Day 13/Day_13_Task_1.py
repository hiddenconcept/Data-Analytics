#In this challenge:
#your objective is to demonstrate your proficiency in creating arrays from lists and extracting specific information from those arrays.
#You have the following data:
names = ["John","Kelly","Jos","Peter","Robert","Piper"]
age = [21,21,56,44,56,96]
gender =[ 'M','F','M','M','M','F']

#1Using the data above, create an array and transpose it. The creation of an array and transposition should be combined into one code. The code should return a transposed array.

import numpy as np

arr = np.array([names,age,gender]).T
print("\n Array:\n", arr)
