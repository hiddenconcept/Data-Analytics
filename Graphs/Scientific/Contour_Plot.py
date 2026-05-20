# Contour Plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.figure(figsize=(8, 6))
cp = plt.contour(X, Y, Z, levels=15, cmap='coolwarm')
plt.colorbar(cp)
plt.title('Contour Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
# levels — number of contour lines
# cmap   — color map used for the lines
# colorbar — shows the scale of values