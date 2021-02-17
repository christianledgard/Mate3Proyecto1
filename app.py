import networkx as nx
import matplotlib.pyplot as plt

import fw
import dijkstra as dj


def construirGrafo(matrix):
    g = nx.DiGraph()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                continue
            g.add_edge(i, j, weight=matrix[i][j])
    return g


matriz_de_adyacencia = [[0, 219, 229, 0, 751, 769, 0],
                        [219, 0, 351, 692, 633, 0, 331],
                        [229, 351, 0, 0, 853, 877, 0],
                        [0, 692, 0, 0, 126, 124, 502],
                        [751, 633, 853, 126, 0, 60, 428],
                        [769, 644, 877, 124, 60, 0, 427],
                        [0, 331, 0, 502, 428, 427, 0]
                        ]

N = 7

print("--- DIJKSTRA ---")
dj.dijkstra(matriz_de_adyacencia, src=0, dest=6)
print("--- Floyd Warshall ---")
fw.floydWarshall(matriz_de_adyacencia, N)

g = construirGrafo(matriz_de_adyacencia)
pos = nx.spring_layout(g)
nx.draw_networkx(g, with_labels=True, pos=pos, node_size=300, node_color="c")
nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=nx.get_edge_attributes(g, 'weight'))
plt.axis("off")
plt.show()


