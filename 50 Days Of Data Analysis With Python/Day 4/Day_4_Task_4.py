#Using numpy, create a 1 dimensional array of 100 random integers from 0 to 10. Use the arry to create a histogram of the data
# and calculate the median and mode. Ensure the results are reproducible

import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)

arr1 = np.random.randint(0,11,100)

#median and mode

median = np.median(arr1)
values, counts = np.unique(arr1, return_counts=True)
mode = values[np.argmax(counts)]
mode_count = counts[np.argmax(counts)]

print("\nArray 1")
print(arr1)
print()
print("Median", median)
print()
print("Mode:", mode, "| Count:", mode_count)


# Create histogram
plt.figure(figsize=(8, 5))
plt.hist(arr1, bins=11, range=(0, 10), edgecolor='black', color='steelblue')
plt.title("Histogram of 100 Random Integers (0-10)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.xticks(range(0, 11))
plt.show()
