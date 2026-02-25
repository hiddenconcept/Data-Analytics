#4.	Here is a list below:

list1 = [[12, 23, 34, 34], [13, 13, 20, 21]]

#Create an array from the list above

import numpy as np

arr = np.array(list1)

unique, counts = np.unique(arr, return_counts=True)

print("\nOriginal Array:\n",arr)

print("\nUnique values:\n",unique)

print("\nUnique counts:\n",counts)

