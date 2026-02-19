#Write a code to slice row 1 from the swapped array in question 3

import numpy as np

arr1= np.arange(0,10).reshape(2,5)
arr2= np.arange(0,10).reshape(5,2)
arr3 = arr1 + arr2.reshape(2,5)
arr4 = np.swapaxes(arr1,0,1)

print("\nOriginal Array 1:\n",arr1)
print("\nSliced Row 1:\n",arr1[0:1])
print("\nOriginal Array 4:\n",arr4)
print("\nSliced Row 1:\n",arr4[0:1])
