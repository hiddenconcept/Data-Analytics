#2.	Using NumPy slicing, write a code that slices these numbers in this order [8, 12, 56] from the array sorted by columns (question 1). Create a new variable.

list1 = [[12, 34, 56], [12, 13, 8,], [6, 5, 10]]

import numpy as np

arr = np.array(list1)

print("\nOriginal Array\n", arr)

col_sorted = np.sort(arr,axis=0)

sliced = col_sorted[[0,1,2],[2,0,2]]

row_sorted = np.sort(arr,axis=1)

print("Sorted by Rows Array: \n", row_sorted)

print("Sorted by Columns Array: \n", col_sorted)


print("\nSliced Array of Columns\n", sliced)

