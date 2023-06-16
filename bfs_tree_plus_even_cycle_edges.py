
from typing import Dict, List


def get_graph_edges(G: List[List[int]]):
    edges = []
    for i in range(len(G)):
        for j in range(i, len(G[i])):
            if G[i][j] == 1:
                edges.append((i, j))
    return edges

def get_pi_edges(tree: Dict[int, int]):
    pi_edges = []
    for vertex in tree.keys():
        pi_edges.append((tree[vertex], vertex))
    return pi_edges

def get_remainder_edges(tree: Dict[int, int], graph: List[List[int]]):
    edges = get_graph_edges(graph)
    pi_edges = get_pi_edges(tree)
    remainder_edges = [edge for edge in edges if edge not in pi_edges and (edge[1], edge[0]) not in pi_edges]
    return remainder_edges

def get_bigger_bipartition(graph, tree):
    bigger_bipartition_edges = get_graph_edges(graph)
    remainder_edges = get_remainder_edges(tree, graph)
    for edge in remainder_edges:
        x = edge[0]
        y = edge[1]
        for distance in graph.distances[x][y]:
            if distance + 1 % 2:
                bigger_bipartition_edges.append(edge)
    return bigger_bipartition_edges

def get_k_edges(graph, tree):
    graph_edges = get_graph_edges(graph)
    bigger_bipartition_edges = get_bigger_bipartition(graph, tree)
    return [edge for edge in graph_edges if edge not in bigger_bipartition_edges and (edge[1], edge[0]) not in bigger_bipartition_edges]
