#6.	Write code to find the outlier in the array above.

nums = [12,4,6,7,9,19,21,67,8]

import numpy as np

arr = np.array(nums)
min = np.min(arr)
npmax = np.argmax(arr)
max = np.max(arr)
avg = np.mean(arr)
new_arr = np.array([np.max(arr), np.min(arr)])
median = np.median(arr)
std_val = np.std(arr)

print("\nOne Dimensional Array: \n",arr)
print("\nNew Array: \n",new_arr)
print("\nMean of Array: \n",avg)
print("\nMedian of Array: \n",median)
#Displaying the true/ false values in this one
print("\nOutlier of Array: \n", arr > (avg + std_val))
print("\nOutlier of Array: \n", arr[arr > (avg + std_val)])