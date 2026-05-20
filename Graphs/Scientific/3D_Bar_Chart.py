# 3D Bar Chart
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = [10, 25, 40, 55, 70]

ax.bar3d(x, y, 0, 0.5, 0.5, z, color='steelblue', alpha=0.8)
ax.set_title('3D Bar Chart')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Values')
plt.show()
# bar3d(x, y, z_bottom, dx, dy, dz)
# dx, dy — width and depth of each bar
# dz     — height of each bar