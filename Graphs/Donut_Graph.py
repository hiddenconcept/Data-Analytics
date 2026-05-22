import matplotlib.pyplot as plt

labels = ['Category 1', 'Category 2', 'Category 3']
sizes = [30, 45, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        wedgeprops=dict(width=0.5))

plt.title('Donut Chart')
plt.show()