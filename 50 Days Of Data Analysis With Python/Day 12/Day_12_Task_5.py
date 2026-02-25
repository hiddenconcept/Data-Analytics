#5.	Using the np.flatten() function to flatten the nested array you created in question 4

list1 = [[12, 23, 34, 34], [13, 13, 20, 21]]

#Create an array from the list above.

import numpy as np

arr = np.array(list1)

#Flatten always flats all of the items within a array.
flattened = arr.flatten()


print("\nOriginal Array:\n",arr)


print("\nFlattened Array:\n",flattened)



