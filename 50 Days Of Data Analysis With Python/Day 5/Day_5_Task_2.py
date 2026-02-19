#Using Numpy,write code to multiply each element in the array you created in question 1 by 2.
#Create a new variable for this array

import numpy as np

list_numbers = [[12,23,-45],[18,-77,-44]]

#creating an array
arr = np.array(list_numbers)
arr_doubled = arr*2

#Displaying our negative numbers
negative_numbers = arr[arr < 0]


print("\nOriginal Array:\n", arr)
print("\nNegative numbers:", negative_numbers)
print("\nOriginal Doubled Array:\n", arr_doubled)
