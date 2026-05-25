# Error Bar Plot
import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D', 'E']
values = [12, 55, 63, 24, 90]
errors = [3, 7, 5, 4, 9]

plt.figure(figsize=(8, 6))
plt.errorbar(categories, values, yerr=errors, fmt='o', color='steelblue',
             ecolor='tomato', elinewidth=2, capsize=6)
plt.title('Error Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
# fmt='o' — marker shape at each data point
# ecolor — color of the error bars
# capsize — width of the caps at the end of error bars