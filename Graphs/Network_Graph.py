import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

# Add nodes
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])

# Add edges (connections)
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'),
                  ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A')])

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(8, 6))
nx.draw(G, pos,
        with_labels=True,
        node_color='steelblue',
        node_size=1500,
        font_size=14,
        font_color='white',
        font_weight='bold',
        edge_color='gray',
        width=2)

plt.title('Network Graph', fontsize=16, fontweight='bold')
plt.show()
# with_labels     — displays node names
# node_size       — size of each node circle
# spring_layout   — positions nodes using a force-directed algorithm
# install with: pip install networkx