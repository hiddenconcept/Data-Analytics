#Using slicing, create a subset array of 3 integers from the array you created in question 1.
#The first integer is at index 2, the second integer is at index 4, and the third index is at index 7.


import numpy as np

np.random.seed(0)
arr = np.random.randint(0,21,size= 10)

#same as before but added the fancy indexing , is the indexed the question was asking for. inside the [[]]
print("\nArray :\n", arr[[2,4,7]])
