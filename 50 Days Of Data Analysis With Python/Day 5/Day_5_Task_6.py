#Write a code to slice row [50,51,52,53,54,55,56,57,58,59] from the array in Question 6.


import numpy as np

arr = np.arange(100,).reshape(2,5,10)

row = arr[1, 0, :]

print(arr)

print("\nSliced Row:", row)

