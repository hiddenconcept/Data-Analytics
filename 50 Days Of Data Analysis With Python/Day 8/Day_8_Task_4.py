#Create a three-dimensional array from the nested list below:

list1 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[11, 12, 13, 14, 15]]]
#           row1             row2            row3

#Using slicing, write code that creates a sublist from the array you created.
# Your code should return an array of numbers (4, 8, and 15).

 #We want columns 4, 2 4 for our numbers

import numpy as np

arr = np.array(list1)

print("\nOriginal Array:\n",arr)

print("\nShape of Original Array:\n",arr.shape)

print("Shape of Original Array:\n",arr.ndim)

print("\nSliced Array:\n", arr[0, [0, 1, 2], [3, 2, 4]])
