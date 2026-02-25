#3.	Create a 2-dimensional array of random integers between

import numpy as np

np.random.seed(42)

# Create 3x3 array of random integers between -100 and 100
rand_arr = np.random.randint(-100,101,size=(3,3))

cleaned_arr = np.where(rand_arr < 0, 0,rand_arr)

print("\nOriginal Array:\n",rand_arr)

print("\nCleaned Array:\n",cleaned_arr)
