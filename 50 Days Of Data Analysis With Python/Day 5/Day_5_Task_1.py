#Using Numpy, create an array from the list. Write a code to return all the negative numbers in the list

import numpy as np

list_numbers = [[12,23,-45],[18,-77,-44]]

#creating an array
arr = np.array(list_numbers)

#Displaying our negative numbers
negative_numbers = arr[arr < 0]


print("\nArray:\n", arr)
print("\nNegative numbers:", negative_numbers)