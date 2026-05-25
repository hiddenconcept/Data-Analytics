# Stem Plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.stem(x, y, linefmt='steelblue', markerfmt='o', basefmt='black')
plt.title('Stem Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()
# linefmt — color/style of the vertical lines
# markerfmt — marker style at the top of each stem
# basefmt — style of the horizontal baseline