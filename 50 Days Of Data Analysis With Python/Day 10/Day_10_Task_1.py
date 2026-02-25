#In this challenge, you will use the NumPy arange() function.
# It is similar to the built-in range() function in Python, but it returns a NumPy array. Boolean indexing, on the other hand, is a way of indexing NumPy arrays based on a set of Boolean conditions.
# It allows you to select elements from an array that meet certain criteria. num = 50


#1.	Create an array from the number above using the arange() function of NumPy. Your array should start at 0 with a step of 5.


import numpy as np

arr = np.arange(0,51,5)
print("\nArray:\n", arr)