import matplotlib.pyplot as p1t
import pit

labels = ['Category 1', 'Category 2', 'Category 3']
sizes = [ 30, 45, 25]

p1t.pie(sizes, labels=labels, autopct='%1.1f%%')
p1t.title('Pie Chart')
p1t.show()