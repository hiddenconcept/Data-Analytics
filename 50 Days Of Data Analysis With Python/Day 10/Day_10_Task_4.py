#In this challenge, you will use the NumPy arange() function.
# It is similar to the built-in range() function in Python, but it returns a NumPy array. Boolean indexing, on the other hand, is a way of indexing NumPy arrays based on a set of Boolean conditions.
# It allows you to select elements from an array that meet certain criteria. num = 50

days = ["Monday", "Tuesday",  "Wednesday",  "Thursday", "Friday"]
hours_worked = [ 8, 8, 10, 11, 7]

#4.	Write another code (using Boolean indexing) to return the day of the week with the highest number of hours worked.

import numpy as np

hours_worked = np.array(hours_worked)
days = np.array(days)

result = days[hours_worked == np.max(hours_worked)]

print("\nDay with most hours:\n", result)