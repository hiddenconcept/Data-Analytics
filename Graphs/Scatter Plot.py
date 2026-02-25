import matplotlib.pyplot as plt
import numpy as np

x =np.random.random(50)
y = 2 * 1 + 0.1 * np.random.random(50)

plt.scatter(x,y)
plt.title('Scatter Plot')
plt.xlabel('Amount')
plt.ylabel('Sales')
plt.show()

