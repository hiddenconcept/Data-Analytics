#Create a one-dimensional array with random integers between 0 and 20.
#The size of the array is 10. Ensure that the results are reproducible.

import numpy as np

np.random.seed(0)
arr = np.random.randint(0,21,size= 10)

print("\nArray :\n", arr)
