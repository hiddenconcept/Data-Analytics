#Write a code to change the data type of the array you just created in question 1(Below) to a floating data type.
#Save this as anew variable

import numpy as np

list_str = ["23","12","90","28","30"]


arr = np.array(list_str,dtype=int)

arr_float = arr.astype(float)

print()
print(list_str)
print()

print("Original Array:" ,arr)
print("Data type", arr.dtype)
print()
print("New Array:" ,arr)
print("Data type", arr_float.dtype)

