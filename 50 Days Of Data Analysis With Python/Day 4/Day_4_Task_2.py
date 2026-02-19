#write a code to add 2 arrays you just created in quesiton 1. Check the shape of the resulting array. EXplain why
#the resulting array is that of the bigger array form the two arrays created in question 1

import numpy as np

np.random.seed(0)
#Sets the arrays

arr1 = np.random.randint(10,21,(2,3))

arr2 = np.random.randint(10,21,(1,3))

result = arr1+arr2

print("\nArray 1:")
print(arr1.shape)
print("\nArray 2:")
print(arr2.shape)
print("\nResult:")
print(result.shape)

#Display the arrays
print("\nArray 1:")
print(arr1)
print("\nArray 2:")
print(arr2)


print("Results:")
print()
print(result)
print()

print("Explain why the resulting array is that of the bigger array form the two arrays created in question 1:")
print()
print("When you add a (1,3) array to a (2,3) array, NumPy automatically stretches `arr2` to match the bigger shape:")