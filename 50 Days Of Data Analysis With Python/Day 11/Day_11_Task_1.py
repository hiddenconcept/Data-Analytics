#1.	Using NumPy, create an array using the list above. Write a code to check how many non-numeric elements are in the list.

list1 = ["34", "name",  "45",  "is",  "100"]

import numpy as np

arr =np.array(list1)
count = 0
for element in arr:
    print(element, element.isnumeric())
    if not element.isnumeric():
        count += 1

print("\nNumber of non-numeric elements is :\n", count)

