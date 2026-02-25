import numpy as np

# start number is what the array starts at, stop is where it ends
#the num on this function, indicates how many number within the stops between the 2 previous numbers,
# so we can manipulate this to get random numbers , to even pull out of the stacks generated.
arr = np.linspace(1,10,6)
#np.array stacks the nested function above
arr2 = np.array(arr)*2

arr3 = np.array(arr)*4

result = np.vstack((arr,arr2,arr3))

#messing around with some information functions, data can change when the numbers change
avg = np.mean(result)
std = np.std(result)
min = np.min(result)
max = np.max(result)

print("\nArray 1:\n",result[0])

print("\nArray 2:\n",result[1])

print("\nArray 3:\n",result[2])

print("\nCombined Generated Array:\n", result)

print("\nGenerated Array's Average:\n", avg)

print("\nGenerated Row Averages :", np.mean(result,axis=1))

print("\nGenerated Column Averages :", np.mean(result,axis=0))

print("\nGenerated Row Standard Deviations :", np.std(result,axis=1))

print("\nGenerated Column Standard Deviations :", np.std(result,axis=0))

print("\nGenerated Array's Minimum Value:",np.min(result))

print("\nGenerated Array's Maximum Value:",np.max(result))


