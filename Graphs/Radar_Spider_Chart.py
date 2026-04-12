import matplotlib.pyplot as plt
import numpy as np

categories = ['Speed', 'Strength', 'Defense', 'Attack', 'Stamina']
values = [80, 65, 90, 75, 85]

# Number of variables
N = len(categories)

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

# Close the plot by repeating first value
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, values, color='steelblue', linewidth=2)
ax.fill(angles, values, color='steelblue', alpha=0.3)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)
ax.set_title('Radar/Spider Chart', fontsize=16, fontweight='bold')
plt.show()
# polar=True — enables circular/polar axis
# angles    — evenly spaced points around the circle
# fill      — shades the area inside the chart