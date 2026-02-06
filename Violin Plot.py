import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
data = [np.random.normal(0,std,100)for std in range(3)]
sns.violinplot(data=data)
plt.title('Violin Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()