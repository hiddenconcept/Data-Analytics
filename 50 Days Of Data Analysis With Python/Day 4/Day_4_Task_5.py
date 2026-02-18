#USing numpy, create a 3 dimensional array of 100 random floats between 0 and 1. Use the array to create a 3d platter
#plot of the data.; Ensure that your results are reproducible.

import numpy as np
import matplotlib.pyplot as plt

# Reproducibility
np.random.seed(0)


# For exactly 100 floats in 3D we use shape (5, 4, 5) = 100
arr1 = np.random.uniform(0, 1, (5, 4, 5))

# Flatten to get x, y, z coordinates for scatter plot
x = arr1[:, :, 0].flatten()
y = arr1[:, :, 1].flatten()
z = arr1[:, :, 2].flatten()

# 3D scatter plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c=z, cmap='viridis', marker='o')

ax.set_title("3D Scatter Plot of Random Floats")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()