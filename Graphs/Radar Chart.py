import numpy as np
import matplotlib.pyplot as plt

labels = np.array(['A','B','C','D','E'])
data = np.array([1,2,3,4,5,6])


angels = np.linspace(0,2*np.pi, len(labels), endpoint=False)
data = np.concatenate((data, [data[0]]))
angels = np.concatenate((angels, [data[0]]))


plt.polar(data, angels)
plt.fill(angels, data,alpha=0.25)
plt.title('Polar Chart')

plt.show()
