#Write a code to perform a dot operation on the arrays

import numpy as np

np.random.seed(0)
#Sets the arrays

arr1 = np.random.randint(10,21,(2,3))

arr2 = np.random.randint(10,21,(1,3))

#transposed "T"
result = np.dot(arr1, arr2. T)


print("\nArray 1:")
print(arr1)
print()
print("\nArray 2:")
print(arr2)
print()
print("Shape of Arr1:", arr1.shape)
print("Shape of Arr2:", arr2.shape)
print()
print("The Result Of The Dot Product:")
print(result)
print()
print("The Shape Of The Dot Product:", result.shape)
