import unittest
from graph import Graph

class TestGraph(unittest.TestCase):

    def test_is_bipartite_dfs(self):
        # Test a bipartite graph
        g = Graph(4)
        g.graph = [[0, 1, 0, 1],
                   [1, 0, 1, 0],
                   [0, 1, 0, 1],
                   [1, 0, 1, 0]]
        self.assertTrue(g.is_bipartite_dfs())

        # Test a non-bipartite graph
        g = Graph(3)
        g.graph = [[0, 1, 1],
                   [1, 0, 1],
                   [1, 1, 0]]
        self.assertFalse(g.is_bipartite_dfs())

        # Test a graph with disconnected components
        g = Graph(5)
        g.graph = [[0, 1, 0, 1, 0],
                   [1, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0],
                   [1, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0]]
        self.assertTrue(g.is_bipartite_dfs())

    def test_is_bipartite_bfs(self):
        # Test a bipartite graph
        g = Graph(4)
        g.graph = [[0, 1, 0, 1],
                   [1, 0, 1, 0],
                   [0, 1, 0, 1],
                   [1, 0, 1, 0]]
        self.assertTrue(g.is_bipartite_bfs())

        # Test a non-bipartite graph
        g = Graph(3)
        g.graph = [[0, 1, 1],
                   [1, 0, 1],
                   [1, 1, 0]]
        self.assertFalse(g.is_bipartite_bfs())

        # Test a graph with disconnected components
        g = Graph(5)
        g.graph = [[0, 1, 0, 1, 0],
                   [1, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0],
                   [1, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0]]
        self.assertTrue(g.is_bipartite_bfs())

if __name__ == '__main__':
    unittest.main()