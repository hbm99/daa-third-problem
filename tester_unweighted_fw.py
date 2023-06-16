import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def test_unweighted_floyd_warshall(self):
        # Test case 1
        graph1 = [[0, 1, 0, 0],
                  [1, 0, 1, 0],
                  [0, 1, 0, 1],
                  [0, 0, 1, 0]]
        g1 = Graph(4, graph1)
        distances1 = {0: [0, 1, 2, 3],
                      1: [1, 0, 1, 2],
                      2: [2, 1, 0, 1],
                      3: [3, 2, 1, 0]}
        self.assertEqual(g1.unweighted_floyd_warshall(), distances1)

if __name__ == '__main__':
    unittest.main()