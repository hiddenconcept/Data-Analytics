#CReate two arrays of random integers between 10,20. the shape of the array must be (2,3) for the first array and (1,3)
# on the second array. check the shape of the arrays ensure that the results are reproducibility

import numpy as np


#Set for reproducibility   remove this to make it be random numbers in the arrays every time
np.random.seed(100)

#Sets the arrays
arr1 = np.random.randint(10,21,(2,3))


arr2 = np.random.randint(10,21,(1,3))

#Check the shapes
print("Shape of Arc1:", arr1.shape)
print("Shape of Arc2:", arr2.shape)

#Display the arrays
print("\nArray 1:")
print(arr1)
print("\nArray 2:")
print(arr2)

print()


#adding them both together
print("Results :")
print(arr1+arr2)