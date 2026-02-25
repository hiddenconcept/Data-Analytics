#In this challenge, you will use the NumPy arange() function.
# It is similar to the built-in range() function in Python, but it returns a NumPy array. Boolean indexing, on the other hand, is a way of indexing NumPy arrays based on a set of Boolean conditions.
# It allows you to select elements from an array that meet certain criteria. num = 50

days = ["Monday", "Tuesday",  "Wednesday",  "Thursday", "Friday"]
hours_worked = [ 8, 8, 10, 11, 7]

#5.	Write another code to return all the days of the week where over 9 hours of work were achieved.

import numpy as np

hours_worked = np.array(hours_worked)
days = np.array(days)

result = days[hours_worked > 9]

print("\nAll of the days with work above 9 hours:\n", result)