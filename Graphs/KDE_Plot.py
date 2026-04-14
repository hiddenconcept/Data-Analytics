import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

data = np.random.normal(0, 1, 1000)

kde = gaussian_kde(data)
x = np.linspace(data.min(), data.max(), 1000)

plt.figure(figsize=(8, 6))
plt.plot(x, kde(x), color='steelblue', linewidth=2)
plt.fill_between(x, kde(x), alpha=0.4, color='steelblue')

plt.title('KDE Plot')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()