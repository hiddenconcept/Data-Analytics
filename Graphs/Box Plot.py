import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

data = [np.random.normal(0,std,100) for std in range(1,12)]
sns.boxplot(data=data)
plt.title('Box Plot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()