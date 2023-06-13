import unittest
from backtrack_solution import backtrack_solution, Graph

class TestBacktrackSolution(unittest.TestCase):
    def test_backtrack_solution(self):
        # Test case 1: Graph with no edges
        g = Graph(3)
        self.assertTrue(backtrack_solution(g, 2))

        # Test case 2: Graph with edges but no bipartition
        g = Graph(4)
        g.graph = [[0, 1, 1, 1],
                   [1, 0, 1, 0],
                   [1, 1, 0, 1],
                   [1, 0, 1, 0]]
        self.assertFalse(backtrack_solution(g, 3))

        # Test case 3: Graph with bipartition
        g = Graph(4)
        g.graph = [[0, 1, 1, 0],
                   [1, 0, 0, 1],
                   [1, 0, 0, 1],
                   [0, 1, 1, 0]]
        self.assertTrue(backtrack_solution(g, 2))

        # Test case 4: Graph with multiple bipartitions
        g = Graph(5)
        g.graph = [[0, 1, 1, 0, 0],
                   [1, 0, 0, 1, 0],
                   [1, 0, 0, 1, 0],
                   [0, 1, 1, 0, 1],
                   [0, 0, 0, 1, 0]]
        self.assertTrue(backtrack_solution(g, 2))
        self.assertTrue(backtrack_solution(g, 3))

if __name__ == '__main__':
    unittest.main()