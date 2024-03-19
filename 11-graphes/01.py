import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()  # non orienté
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
matrice = nx.adjacency_matrix(g)
print(1-matrice.todense())

nx.draw_networkx(g, node_color='#FF0000', edge_color='#00FF00')
plt.show()
