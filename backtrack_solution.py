
from itertools import combinations
from graph import Graph


def backtrack_solution(g, k):

    def check_bipartition(comb):
        new_g = Graph(g.V)
        new_g.graph = [[g.graph[i][j] for j in range(g.V)] for i in range(g.V)]
        for edge in comb:
            x = edge[0]
            y = edge[1]
            new_g.graph[x][y] = 0
            new_g.graph[y][x] = 0
        return new_g.is_bipartite_dfs()

    def remove_k_edges(edges, k):
        for comb in combinations(edges, k):
            if check_bipartition(comb):
                return True
        
    is_bipartite = False
    edges = []
    for i in range(g.V):
        for j in range(i + 1, g.V):
            if g.graph[i][j]:
                edges.append((i, j))
    if k >= len(edges):
        return True
    else:
        is_bipartite = remove_k_edges(edges, k)
    return is_bipartite