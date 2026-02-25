#The skill to sort arrays in ascending or descending order and filter arrays to include only elements that meet certain criteria is a useful skill for organizing data or identifying patterns in the data.
# These skills will be tested with the challenges below:
list1 = [[12, 34, 56], [12, 13, 8,], [6, 5, 10]]
#1.	Create an array using the list above. Write code to sort the array in ascending order:
# first sort by columns, then by rows. Create a new variable for each of the sorted arrays.


import numpy as np

arr = np.array(list1)

print("\nOriginal Array\n", arr)

col_sorted = np.sort(arr,axis=0)

print("Sorted by Columns Array: \n", col_sorted)

row_sorted = np.sort(arr,axis=1)
print("Sorted by Rows Array: \n", row_sorted)