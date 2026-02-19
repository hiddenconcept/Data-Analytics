#Using the arange() function, crate an array of numbers of 0 to 10.
#The shape must be (2,5)

import numpy as np

arr = np.arange(0,10).reshape(2,5)
print(arr)