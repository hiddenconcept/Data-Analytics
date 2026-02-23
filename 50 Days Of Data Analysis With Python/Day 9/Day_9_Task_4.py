#Using NumPy, calculate the average of the biggest and smallest numbers in the array.
nums = [12,4,6,7,9,19,21,67,8]

import numpy as np

arr = np.array(nums)
min = np.min(arr)
npmax = np.argmax(arr)
max = np.max(arr)
avg = np.mean(arr)
new_arr = np.array([np.max(arr), np.min(arr)])

print("\nOne Dimensional Array: \n",arr)
print("\nNew Array: \n",new_arr)
print("\nThe Average for the biggest & smallest in the Array:\n",np.mean(new_arr))
