import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E', 'F']
values1 = [12, 55, 63, 24, 90, 54]
values2 = [30, 20, 45, 60, 15, 40]
values3 = [18, 35, 22, 50, 30, 25]

plt.bar(categories, values1, label='Series 1', color='steelblue')
plt.bar(categories, values2, bottom=values1, label='Series 2', color='tomato')
plt.bar(categories, values3, bottom=[v1 + v2 for v1, v2 in zip(values1, values2)],
        label='Series 3', color='gold')

plt.title('Stacked Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.show()