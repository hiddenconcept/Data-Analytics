#2.	Using NumPy, write code to sum all the numeric elements in the list.

list1 = ["34", "name",  "45",  "is",  "100"]

import numpy as np

numeric_array1 = np.array([int(x) for x in list1 if x.isnumeric()])

total = np.sum(numeric_array1)

print("\nNumeric Elements:\n",numeric_array1)
print("\nSum Total:\n",total)