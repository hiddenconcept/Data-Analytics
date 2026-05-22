import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E', 'F']
values = [12, 55, 63, 24, 90, 54]

plt.barh(categories, values)
plt.title('Horizontal Bar Chart')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.show()