#Create a Numpy array using the list above. Calculate the standard deviation of the array

import numpy as np

list_str = ["23","12","90","28","30"]


arr = np.array(list_str,dtype=int)

std_dev = np.std(arr)

print("Array:" ,arr)
print()
print(list_str)
print()
print("standard Deviation:" ,std_dev)
