import numpy as np

arr = np.random.randint(1,10,10)

arr4 = np.array(arr*4) /2
arr2 =np.array(arr) *2
arr3 = np.array(arr) *4



result = np.vstack((arr,arr2,arr3,arr4))

print("\nArray 1:\n",arr)

print("\nArray 2:\n",arr2)

print("\nArray 3:\n",arr3)

print("\nArray 4:\n",arr4)

print("\nCombined Generated Array 4:\n",result)

print("\nShape of Generated Array :\n", np.shape(result))

print("\n Size of Generated Array :\n", np.size(result))

