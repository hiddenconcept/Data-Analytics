import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data =np.random.rand(6,10)
sns.heatmap(data, annot=True)
plt.title('Heat Map')
plt.show()