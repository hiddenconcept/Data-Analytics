import matplotlib.pyplot as plt
x = list(range(0,5))
y = [2,9,56,95,6]

#matplotlib requires both lists to have the same length

plt.plot(x,y)
plt.title('Sales By The Quarterly')
plt.xlabel('Amount')
plt.ylabel('Sales')

plt.show()