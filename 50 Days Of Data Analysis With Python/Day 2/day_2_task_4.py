#create an array from the three list. take note on that some of the lists contain floats. create an array that will have an int64 data type.
import numpy as np

list1 = [2,3,4,6]
list2 = [8,10.1,12,14]
list3 = [16,18,20,22.1]

arr = np.array([list1,list2,list3])
#adding the no.rint gives more control over how the floats become integers instead of letting them be silently chopped off
arr = np.rint(arr).astype(np.int64)

print("Array is:")
print(arr)


print("\nShape is:",arr.shape)
print("Dimension is:",arr.ndim)
print("Data types",arr.dtype)
