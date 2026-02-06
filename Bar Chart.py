import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E', 'F']

values = [12,55,63,24,90,54]

plt.bar(categories, values)
plt.title('Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()