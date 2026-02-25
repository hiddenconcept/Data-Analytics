import matplotlib.pyplot as plt
import numpy as np

data = np.random.random(1000)

plt.title('Histogram')
plt.hist(data, bins=25,edgecolor='black', facecolor='lightgreen')
plt.xlabel('Random Value')
plt.ylabel('Frequency')
plt.show()

# bin value changes the number of the bars
#edgecolor changes the edge border of the bar
#faceoclour changes the face value