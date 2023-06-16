import unittest
from graph import Graph

class TestBFSTree(unittest.TestCase):
    def test_bfs_tree(self):
        # Test case 1
        g1 = Graph(6)
        # g1.add_edge(0, 1)
        # g1.add_edge(0, 2)
        # g1.add_edge(1, 3)
        # g1.add_edge(1, 4)
        # g1.add_edge(2, 4)
        # g1.add_edge(3, 5)
        # g1.add_edge(4, 5)
        g1.graph = [[0, 1, 1, 0, 0, 0],
                    [1, 0, 0, 1, 1, 0],
                    [1, 0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0, 1],
                    [0, 1, 1, 0, 0, 1],
                    [0, 0, 0, 1, 1, 0]]
        self.assertEqual(g1.bfs_tree(0), {1: 0, 2: 0, 3: 1, 4: 1, 5: 3})

        # Test case 2
        g2 = Graph(4)
        # g2.add_edge(0, 1)
        # g2.add_edge(0, 2)
        # g2.add_edge(1, 2)
        # g2.add_edge(2, 3)
        g2.graph = [[0, 1, 1, 0],
                    [1, 0, 1, 0],
                    [1, 1, 0, 1],
                    [0, 0, 1, 0]]
        self.assertEqual(g2.bfs_tree(0), {1: 0, 2: 0, 3: 2})

        # Test case 3
        g3 = Graph(5)
        # g3.add_edge(0, 1)
        # g3.add_edge(0, 2)
        # g3.add_edge(1, 2)
        # g3.add_edge(2, 3)
        # g3.add_edge(3, 4)
        g3.graph = [[0, 1, 1, 0, 0],
                    [1, 0, 1, 0, 0],
                    [1, 1, 0, 1, 0],
                    [0, 0, 1, 0, 1],
                    [0, 0, 0, 1, 0]]
        self.assertEqual(g3.bfs_tree(0), {1: 0, 2: 0, 3: 2, 4: 3})

if __name__ == '__main__':
    unittest.main()