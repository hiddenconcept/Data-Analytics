import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D', 'E', 'F']
x = [12, 55, 63, 24, 90, 54]
y = [30, 20, 45, 60, 15, 40]
bubble_size = [200, 500, 800, 300, 1000, 600]  # controls bubble size

plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=bubble_size, alpha=0.6, color='steelblue', edgecolors='black')

# Label each bubble
for i, label in enumerate(categories):
    plt.text(x[i], y[i], label, ha='center', va='center', fontsize=10, fontweight='bold')

plt.title('Bubble Chart')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()