import random
from backtrack_solution import find_min_k
from graph import Graph
from max_cross_edges_bipartition import NeighborsGraph, partition

def generate_random_edges(num_vertices, num_edges):
    edges = set()
    # hit_count = 100
    while len(edges) < num_edges:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v:
            edges.add((u, v))
        # if hit_count == 0:
        #     break
        # hit_count -= 1
    return list(edges)

if __name__ == '__main__':

    exact_approaches = 0
    ratio_list = []
    iter = 100
    n = 8
    for _ in range(iter):
        vertex_numbers = random.randint(1, n)
        edge_numbers = random.randint(0, vertex_numbers * (vertex_numbers - 1) // 2)
        edges = generate_random_edges(vertex_numbers, edge_numbers)

        g_Graph = Graph.from_edges(edges)
        g_NeighborsGraph = NeighborsGraph(edges=edges)

        _, _, k_approx = partition(g_NeighborsGraph)

        k_exact = find_min_k(g_Graph)

        if k_exact == k_approx:
            exact_approaches += 1
        else:
            ratio_list.append((k_approx + 1)/(k_exact + 1)) # to avoid division by 0

    print('Exact approaches: ' + str(exact_approaches) + '/' + str(iter))
    print('Average ratio (k from k-approx): ' + str(sum(ratio_list)/len(ratio_list)) + ' (lower is better)')
