#Write a code to return the sum of values [90.0,28.0,30.0] from the array you just created

import numpy as np

list_str = ["23","12","90","28","30"]


arr = np.array(list_str,dtype=int)

arr_float = arr.astype(float)

sum_request = np.sum(arr_float)

print()
print(list_str)
print()
print("Original Array:" ,arr)
print("Data type", arr.dtype)
print()
print("New Array:" ,arr)
print("Data type", arr_float.dtype)
print()
print("Sum of Request: [90.0,28.0,30.0]:", sum_request)



