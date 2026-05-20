# Quiver Plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 10)
y = np.linspace(-3, 3, 10)
X, Y = np.meshgrid(x, y)
U = -Y   # x direction of arrows
V =  X   # y direction of arrows

plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V, color='steelblue')
plt.title('Quiver Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
# U, V — x and y components of the arrow direction
# creates a circular vector field in this example