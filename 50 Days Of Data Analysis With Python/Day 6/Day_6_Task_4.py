#Create a 2-dimensional array of random integers from 0 to 100 with the shape (5,5)
#Use the array to find the minimum and maximum values , as well as the mean and standard deviation.
# Ensure that the results are reproducible

import numpy as np

#makes it reproducible
np.random.seed(0)
#Setting the tone for the array
arr = np.random.randint(0,101,(5,5))

#Setting up our Variables for our Question
mean = np.mean(arr)
std = np.std(arr)
min = np.min(arr)
max = np.max(arr)




print("\nArray:\n",arr)
print("\nMean:",mean)
print("\nStd:",std)
print("\nMin:",min)
print("\nMax:",max)