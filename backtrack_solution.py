
from graph import Graph


def backtrack_solution(g, k):

    def check_bipartition(comb):
        new_g = Graph(g.V)
        for edge in comb:
            x = edge[0]
            y = edge[1]
            new_g.graph[x][y] = 0
            new_g.graph[y][x] = 0
        return new_g.is_bipartite_dfs()

    def no_rep_combinations(lst, k, comb, pos, last, is_bipartite):
        if is_bipartite:
            return
        if pos == len(comb):
            is_bipartite = check_bipartition(comb)
        else:
            for i in range(len(lst)):
                if i >= last:
                    comb[pos] = lst[i]
                    no_rep_combinations(lst, k, comb, pos + 1, i + 1, is_bipartite)

    is_bipartite = False
    edges = [(i, j) for i in range(g.V) for j in range(i + 1, g.V) if g.graph[i][j]]
    no_rep_combinations(edges, k, [None] * k, 0, 0, is_bipartite)
    return is_bipartite

if __name__ == "__main__":
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]]
    k = 2
    print(backtrack_solution(g, k))