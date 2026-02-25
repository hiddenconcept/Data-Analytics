#In this challenge, you will use the NumPy arange() function.
# It is similar to the built-in range() function in Python, but it returns a NumPy array. Boolean indexing, on the other hand, is a way of indexing NumPy arrays based on a set of Boolean conditions.
# It allows you to select elements from an array that meet certain criteria. num = 50

#2.	Using NumPy, write a code that returns all the numbers in the array that are greater than 25.

import numpy as np

arr = np.arange(0,51,5)
print("\nArray:\n", arr)

print("\nNumbers in the Array Bigger then 25:\n", arr[arr>25])
#ADded this to help show comparison
print("\nNumbers in the Array Smaller then 25:\n", arr[arr<25])
