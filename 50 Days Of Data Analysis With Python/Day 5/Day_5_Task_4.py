#Write a code to calculate the sum of numbers on axis-0 of the array you created in question 2

import numpy as np

list_numbers = [[12,23,-45],[18,-77,-44]]



#creating an array
arr = np.array(list_numbers)

arr_doubled = arr*2

axis0_sum = np.sum(arr_doubled, axis=0)

negative_numbers = arr[arr < 0]


#Displaying our negative numbers


print("\nOriginal Doubled Array:\n", arr_doubled)

print("\nNegative numbers:", negative_numbers)

print("\nSum of numbers of axis-0:", axis0_sum)
