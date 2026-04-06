import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Outer ring
outer_labels = ['Electronics', 'Clothing', 'Food', 'Furniture']
outer_values = [40, 25, 20, 15]
outer_colors = ['steelblue', 'tomato', 'gold', 'mediumseagreen']

# Inner ring
inner_labels = ['Phones', 'Laptops', 'Shirts', 'Pants', 'Fruits', 'Vegs', 'Sofas', 'Tables']
inner_values = [25, 15, 15, 10, 12, 8, 10, 5]
inner_colors = ['#5b9bd5', '#2e75b6', '#e8604c', '#c0392b',
                '#f4c430', '#d4a017', '#57b894', '#2e8b57']

outer_angles = np.cumsum([0] + outer_values) / 100 * 2 * np.pi
inner_angles = np.cumsum([0] + inner_values) / 100 * 2 * np.pi

for i in range(len(outer_values)):
    ax.barh(2, outer_angles[i+1] - outer_angles[i],
            left=outer_angles[i], height=0.5,
            color=outer_colors[i], edgecolor='white')

for i in range(len(inner_values)):
    ax.barh(1, inner_angles[i+1] - inner_angles[i],
            left=inner_angles[i], height=0.5,
            color=inner_colors[i], edgecolor='white')

ax.set_axis_off()
ax.set_title('Sunburst Chart', fontsize=16, fontweight='bold')
plt.show()
# barh on polar axis creates arc-shaped segments
# height controls ring thickness
# left controls starting angle of each segment