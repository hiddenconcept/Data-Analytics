#Create an array from two of the lists then write a code a check the shape,dimensions and data type of the array

import numpy as np
list1 = [2,3,4,6]
list2 = [8,10.1,12,14]

arr = np.array([list1,list2])
print("Array is:")
print(arr)

print("\nShape is:",arr.shape)
#Shape → (2, 4)
#(2 rows, 4 columns)

print("Dimension is:",arr.ndim)
#Dimensions (ndim) → 2
#(because it’s a 2D array)

print("Data type:",arr.dtype)
#Data type (dtype) → float64
#(NumPy upcasts to float because list2 contains 10.1)
