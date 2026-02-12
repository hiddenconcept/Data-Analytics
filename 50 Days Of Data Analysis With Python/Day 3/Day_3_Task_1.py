# Using numpy create an array of random numbers between 0 and 1. the shape of the array must be (3,4)\
#Use seed eo ensure that the results are reproducible.

import numpy as np
#Sets a reproducible random seed (seed=24)
rng = np.random.default_rng(seed = 24)
#Creates an array of shape (3, 4)
array = rng.random((3,4))

print(array)