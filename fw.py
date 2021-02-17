def printPath(path, v, u):
    if path[v][u] == v:
        return

    printPath(path, v, path[v][u])
    print(path[v][u], end=' ')


def printSolution(path, n):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                print(f"The shortest path from {v} —> {u} is ({v}", end=' ')
                printPath(path, v, u)
                print(f"{u})")


def convertMatrix(adjency_matrix):
    new_matrix = list()
    for i in adjency_matrix:
        new_row = list()
        for j in i:
            if j == 0:
                new_row.append(float("Inf"))
            else:
                new_row.append(j)
        new_matrix.append(new_row)
    return new_matrix


def floydWarshall(adj_matrix, n):
    adj_matrix = convertMatrix(adj_matrix)

    cost = adj_matrix.copy()
    path = [[0 for x in range(n)] for y in range(n)]

    for v in range(n):
        for u in range(n):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != float('inf'):
                path[v][u] = v
            else:
                path[v][u] = -1

    for k in range(n):
        for v in range(n):
            for u in range(n):
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]

            if cost[v][v] < 0:
                print("Negative-weight cycle found")
                return

    printSolution(path, n)


def minDistance(dist, queue):
    minimum = float("Inf")
    min_index = -1

    for i in range(len(dist)):
        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i
    return min_index

# Este código fue adaptado de https://www.techiedelight.com/pairs-shortest-paths-floyd-warshall-algorithm/
