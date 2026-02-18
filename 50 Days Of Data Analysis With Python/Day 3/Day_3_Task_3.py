#Using numpy, generate an array of 1000 random numbers from a standard normal distrubution with a mean of 0 and
# a variance of 1. create a histogram with this array. Use the seed parameter to ensure the results are reproducbile
import numpy as np
import matplotlib.pyplot as plt

#randomizies
rng = np.random.default_rng(seed = 0)

arr = rng.normal(loc=0 , scale=1, size=1000)

#Displays the information in python screen
print("Mean = ", np.mean(arr))
print("Variance = ", np.var(arr))


#Histogram
plt.hist(arr, bins=72, edgecolor='black')
plt.title("Histogram of random numbers")
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

