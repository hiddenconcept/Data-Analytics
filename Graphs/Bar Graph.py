import matplotlib.pyplot as plt
import seaborn as sns

categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6']
values = [20,30,40,50,60,80]

sns.barplot(x =categories, y =values)
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()
