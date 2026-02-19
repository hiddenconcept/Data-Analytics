#Below are 2 arrays :

first_name = ["John","Kenny"]
last_name = ["Smith","Sakula"]

#Using Numpy's char.join() function , create 2 arrays by joining the first name with the last name .
#Your First array should be John+Smith, dtype =u6. Your second array should be Kenny Sakula, dtype =u6

import numpy as np

first_names = np.array(["John","Kenny"])
last_names = np.array(["Smith","Sakula"])


arr1 = np.array(np.char.add(np.char.add(first_names, "+"), last_names), dtype='U6')
arr2 = np.array(np.char.add(np.char.add(first_names, " "), last_names), dtype='U13')
print()

print()
print("\nCreate 2 arrays by joining the first name with the last name\n"
      "\nYour First array should be John+Smith, dtype =u6\n"
      "Your second array should be Kenny Sakula, dtype =u6")
print()
print("\nArray 1:",arr1)
print("\nArray 2:",arr2)
