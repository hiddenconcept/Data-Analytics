#3.	Write a code that returns the index of the largest number in the array.
nums = [12,4,6,7,9,19,21,67,8]

import numpy as np

arr = np.array(nums)
max = np.argmax(arr)
print("\nOne Dimensional Array: \n",arr)
print("\nMax Value From Array: \n",max)

#np.argmax() returns 7 which is the index position of 67 (the largest number) in the array.
# If wanted just the max number of the array(67) would use np.max()