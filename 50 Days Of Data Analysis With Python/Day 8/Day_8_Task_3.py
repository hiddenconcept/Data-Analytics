#Create a two-dimensional array from the list below. Check the dimensions and shape of your array.

my_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

#Using slicing, write a code to access the numbers 3, 8 and 13. Your code should return [3, 8, 13]

import numpy as np

arr = np.array(my_list)
print("\nArray:", arr)
print("\nShape",arr.shape)
print("\nDimensions",arr.ndim)

print("\nSliced Array :\n", arr[:,2])

print("\nSliced Array :\n", arr[[0, 1, 2], [2, 2, 2]])