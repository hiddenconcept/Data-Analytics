import numpy as np

#This array stacks 1's. it works for other numbers as well.
arr = np.ones(6)

#making a new array and copying the previous one that we have made
arr2 = np.array(arr)

#vpstack function is now stacking our 2 arrays into the same stack, to avoid them using operator functions on them
result = np.vstack((arr,arr2))

print("\nArray:\n", result)

