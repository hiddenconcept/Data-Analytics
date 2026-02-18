#Using random.choice() from numpy, genereate an array from the list above, the shape of the array must be (3,4)
import numpy as np
#Our list of options
fruits = ("Orange","Apple","Pear")

#setting up our main line of code,randoms the fruit choices up top, and our size
arr = np.random.choice(fruits, size=(3,4))
#PRINTS
print(arr)