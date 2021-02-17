import networkx as nx
import matplotlib.pyplot as plt

result_printed = list()


def minDistance(dist, queue):
    minimum = float("Inf")
    min_index = -1

    for i in range(len(dist)):
        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i
    return min_index


def printPath(parent, j, printing=True):
    if parent[j] == -1:
        if printing:
            print(j, end=" ")
        result_printed.append(j)
        return
    printPath(parent, parent[j], printing)
    if printing:
        print(j, end=" ")
    result_printed.append(j)


def printSolution(dist, parent, src):
    for i in range(0, len(dist)):
        if src == i:
            continue
        print("The shortest path from ", src, " -> ", i, " is (", end="")
        printPath(parent, i)
        print(")", "  |  Tiempo Total: ", dist[i])


def drawSolution(graph, parent, i):
    global result_printed
    result_printed = []
    printPath(parent, i, printing=False)

    g = nx.DiGraph()

    for i in range(len(result_printed)-1):
        g.add_edge(result_printed[i], result_printed[i+1], weight=graph[result_printed[i]][result_printed[i+1]])
    pos = nx.spring_layout(g)
    nx.draw_networkx(g, with_labels=True, pos=pos, node_size=300, node_color="c")
    nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=nx.get_edge_attributes(g, 'weight'))
    plt.axis("off")
    plt.show()


def dijkstra(graph, src, dest=0):
    row = len(graph)
    col = len(graph[0])

    dist = [float("Inf")] * row
    parent = [-1] * row
    dist[src] = 0

    queue = []
    for i in range(row):
        queue.append(i)

    while queue:
        u = minDistance(dist, queue)
        queue.remove(u)

        for i in range(col):
            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] < dist[i]:
                    dist[i] = dist[u] + graph[u][i]
                    parent[i] = u

    printSolution(dist, parent, src)
    drawSolution(graph, parent, dest)

# Este codigo fue adaptado de Neelam Yadav
# https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
