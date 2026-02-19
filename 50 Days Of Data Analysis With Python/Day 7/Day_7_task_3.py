#Swap the indexes of the array from question 2 using the swapaxes() method.
# Create a new variable for the swapped array

import numpy as np

arr1= np.arange(0,10).reshape(2,5)
arr2= np.arange(0,10).reshape(5,2)
arr3 = arr1 + arr2.reshape(2,5)
arr4 = np.swapaxes(arr1,0,1)

print("\nOriginal Array:\n",arr1)
print("\nSwapped Axes Array:\n",arr4)