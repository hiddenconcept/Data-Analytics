import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [10,15,20,25,30]
y2 = [20,30,40,50,60]

plt.fill_between(x,y1,y2,color='blue',alpha=0.5)
plt.title('Area Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()
