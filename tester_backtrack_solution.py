import unittest

import matplotlib.pyplot as plt
import networkx as nx

from backtrack_solution import Graph, backtrack_solution


class TestBacktrackSolution(unittest.TestCase):
    def test_backtrack_solution(self):
        # Test case 1: Graph with no edges
        g = Graph(3)
        self.assertTrue(backtrack_solution(g, 2))

        # Example 1: Graph with 4 vertices and 4 edges
        g = Graph(4)
        g.graph = [[0, 1, 1, 1],
                   [1, 0, 1, 0],
                   [1, 1, 0, 1],
                   [1, 0, 1, 0]]
        self.assertTrue(backtrack_solution(g, 1))

        # Example 2: Graph with 5 vertices and 6 edges
        g = Graph(5)
        g.graph = [[0, 1, 1, 0, 0],
                   [1, 0, 0, 1, 1],
                   [1, 0, 0, 1, 0],
                   [0, 1, 1, 0, 1],
                   [0, 1, 0, 1, 0]]
        self.assertFalse(backtrack_solution(g, 0))
        self.assertTrue(backtrack_solution(g, 1))

        # Example 3: Graph with 5 vertices and 8 edges
        g = Graph(5)
        g.graph = [[0, 1, 1, 0, 1],
                   [1, 0, 0, 1, 1],
                   [1, 0, 0, 1, 1],
                   [0, 1, 1, 0, 1],
                   [1, 1, 1, 1, 0]]
        self.assertFalse(backtrack_solution(g, 1))
        self.assertTrue(backtrack_solution(g, 2))

        # petersen_graph = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
        #                   [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        #                   [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        #                   [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        #                   [1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        #                   [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        #                   [0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        #                   [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        #                   [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        #                   [0, 0, 0, 0, 0, 1, 0, 1, 1, 0]]
        petersen_graph = Graph(10)
        petersen_graph.graph = [[0, 1, 1, 0, 0, 0, 0, 1, 1, 0], 
                                [1, 0, 0, 0, 1, 0, 1, 1, 0, 0], 
                                [1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                                [0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                                [0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
                                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
                                [0, 1, 0, 0, 1, 0, 0, 0, 0, 0], 
                                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
                                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]
        # plot_graph(g.graph)
        self.assertFalse(backtrack_solution(petersen_graph, 1))
        self.assertFalse(backtrack_solution(petersen_graph, 2))
        self.assertFalse(backtrack_solution(petersen_graph, 3))
        self.assertFalse(backtrack_solution(petersen_graph, 4))
        self.assertTrue(backtrack_solution(petersen_graph, 5))

def plot_graph(g):
    # Create a networkx graph from the adjacency matrix
    G = nx.Graph()
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 1:
                G.add_edge(i, j)

    # Draw the graph using a circular layout
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True)

    # Show the plot
    plt.show()

if __name__ == '__main__':
    unittest.main()