import matplotlib.pyplot as plt
import squarify

categories = ['Electronics', 'Clothing', 'Food', 'Furniture', 'Toys']
values = [500, 300, 200, 150, 100]
colors = ['steelblue', 'tomato', 'gold', 'mediumseagreen', 'mediumpurple']

plt.figure(figsize=(10, 6))
squarify.plot(sizes=values, label=categories, color=colors,
              alpha=0.8, edgecolor='white', linewidth=2,
              text_kwargs={'fontsize': 12, 'fontweight': 'bold'})
plt.title('Treemap', fontsize=16, fontweight='bold')
plt.axis('off')
plt.show()
# sizes     — determines the size of each rectangle
# label     — text displayed inside each rectangle
# edgecolor — border color between rectangles
# axis off  — hides the axes for a cleaner look
# install with: pip install squarify