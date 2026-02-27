#6.	One of the uses of slicing is for data visualization.
# Slicing is often used in data visualization to extract specific portions of a dataset for plotting.
# Write code to create a subarray of the ages (only ages) in the transposed array using slicing.
# Using Matplotlib, plot a histogram of the age array. Your graph should have an xlabel, an ylabel, and a title.

import numpy as np
import matplotlib.pyplot as plt

names = ["John","Kelly","Jos","Peter","Robert","Piper"]
age = [21,21,56,44,56,96]
gender = ['M','F','M','M','M','F']

# Create transposed array
arr = np.array([names, age, gender]).T
print("\nArray:\n", arr)

# Extract ages using slicing (column index 1, all rows)
ages = arr[:, 1].astype(int)
print("\nAges subarray:", ages)

#histogram
plt.hist(ages, bins=5, color='steelblue', edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of Ages")
plt.show()