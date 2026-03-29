import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

fig, ax = plt.subplots(figsize=(10, 6))

Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=150,
       flows=[1000, -400, -300, -200, -100],
       labels=['Revenue', 'Cost of Goods', 'Marketing', 'Operations', 'Profit'],
       orientations=[0, 1, 0, -1, 0]).finish()

plt.title('Sankey Diagram', fontsize=16, fontweight='bold')
plt.show()
# flows       — positive values are inputs, negative are outputs
# labels      — label for each flow
# orientations— direction of each flow (0=right, 1=up, -1=down)