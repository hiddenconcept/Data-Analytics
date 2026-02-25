#3.	Using NumPy, write code to square all the numeric elements in the array you created in question 1. Return an array of squared elements.

list1 = ["34", "name",  "45",  "is",  "100"]

import numpy as np

arr =np.array(list1)
count = 0
for element in arr:
    print(element, element.isnumeric())
    if not element.isnumeric():
        count += 1

#This is what makes the entire section here work,the extra brackets.
numeric_array1 = np.array([int(x) for x in arr if x.isnumeric()])

squared_array1 = np.square(numeric_array1)

print("\nNumeric Array :\n", numeric_array1)

print("\nSquare Array :\n", squared_array1)

print("\n Numeric Array to Power of 3:\n",np.power(numeric_array1,3))

print("\n Numeric Array to Power of 4:\n",np.power(numeric_array1,4))