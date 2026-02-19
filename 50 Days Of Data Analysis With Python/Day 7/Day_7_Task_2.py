#write a code to change the shape of the array of question 1 to(5,2)
#Crete a new variable for this array. Now add this array to the original array in question 1.
#The result array should have a shape of (2,5). Save this as a new variable

import numpy as np

arr1= np.arange(0,10).reshape(2,5)
arr2= np.arange(0,10).reshape(5,2)
arr3 = arr1 + arr2.reshape(2,5)

print("\nArray 1 :\n" ,arr1)
print("\nArray 2 :\n" ,arr2)
print("\nArray 3 :\n" ,arr3)
