#2.	Using NumPy, write code that returns the minimum number in the array.
nums = [12,4,6,7,9,19,21,67,8]

import numpy as np

arr = np.array(nums)
min = np.min(arr)
print("\nOne Dimensional Array: \n",arr)
print("\nMin Value From Array: \n",min)