#Using the numPy arrange() function, crate a numpy array of numbers from 0 to 99.
#The shape fo the array must be (2,5,10)
import numpy as np

arr = np.arange(100,).reshape(2,5,10)

print(arr)
print("\nShape:", arr.shape)