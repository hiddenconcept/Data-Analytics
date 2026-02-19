#Let's analyze the array you created in question 1(below) further.
#How many numbers in row 1 are greater then the numbers sin row 2?


import numpy as np

list_numbers = [[12,23,-45],[18,-77,-44]]

#creating an array
arr = np.array(list_numbers)

# Extract rows
row1 = arr[0]
row2 = arr[1]

#Comparing
comparison = row1 > row2

#counting
count = np.sum(row1 > row2)


#Displaying our negative numbers
negative_numbers = arr[arr < 0]


print("\nArray:\n", arr)
print("\nNegative numbers:", negative_numbers)
print("\nRow 1:\n", row1)
print("\nRow 2:\n", row2)
print("\nElement-wise comparison:", comparison)
print("\nNumber of elements in Row 1 greater then Row 2:", count)
print()
print("It seem's Row 1 has 2 numbers that are greater then Row 2")