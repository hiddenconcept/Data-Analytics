# Step Plot
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [10, 35, 20, 50, 30, 45]

plt.figure(figsize=(8, 6))
plt.step(x, y, color='steelblue', linewidth=2, where='mid')
plt.fill_between(x, y, step='mid', alpha=0.3, color='steelblue')
plt.title('Step Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()
# where='mid' — step occurs at the midpoint between x values
# fill_between — fills area under the step line