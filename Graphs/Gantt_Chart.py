import matplotlib.pyplot as plt
import numpy as np

tasks = ['Planning', 'Design', 'Development', 'Testing', 'Deployment']
start = [1, 3, 5, 10, 13]
duration = [2, 3, 6, 3, 2]
colors = ['steelblue', 'tomato', 'gold', 'mediumseagreen', 'mediumpurple']

fig, ax = plt.subplots(figsize=(10, 6))

for i, (task, s, d) in enumerate(zip(tasks, start, duration)):
    ax.barh(task, d, left=s, color=colors[i], edgecolor='black', height=0.5)
    ax.text(s + d / 2, i, f'{d} days', ha='center',
            va='center', fontsize=10, fontweight='bold', color='white')

ax.set_xlabel('Days', fontsize=13)
ax.set_title('Gantt Chart', fontsize=16, fontweight='bold')
ax.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
# barh   — horizontal bars representing task duration
# left   — start day of each task
# duration — length of each bar (how long the task takes)