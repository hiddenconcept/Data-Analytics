import numpy as np

#3 dimension array

arr = np.arange(1,10).reshape(3,3)
arr2 = np.arange(10, 19).reshape(3,3)

result = np.hstack((arr,arr))
result2 = np.hstack((arr2,arr))
result3 = np.vstack((arr,arr2))
result4 = np.hstack((arr, arr2))
result5 = np.vstack((arr, arr2))
result6= np.hstack((arr, arr, arr2,arr2))
result7 = np.vstack((arr, arr, arr2,arr2))

print("\nArray 1:\n",arr)

print("\nNew Horizontal Stacked Array :\n",result)

print("\nNew Column Stacked Array 2:\n", result3)

print("\nOrganized Array 2:\n", result2)
print("\nOrganized Array 3:\n", result4)
print("\nOrganized Array 4:\n", result5)
print("\nOrganized Array 5:\n", result6)
print("\nOrganized Array 6:\n", result7)

