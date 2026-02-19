#Write a code to calculate the sum of the numbers on axis-1 of the array you create din question 2

import numpy as np

list_numbers = [[12,23,-45],[18,-77,-44]]



#creating an array
arr = np.array(list_numbers)

arr_doubled = arr*2

axis1_sum = np.sum(arr_doubled, axis=1)


#Displaying our negative numbers
negative_numbers = arr[arr < 0]


print("\nOriginal Doubled Array:\n", arr_doubled)

print("\nNegative numbers:", negative_numbers)

print("\nSum of numbers of axis-1:", axis1_sum)
