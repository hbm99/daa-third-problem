import unittest
from backtrack_solution import find_min_k
from max_cross_edges_bipartition import NeighborsGraph, partition
from graph import Graph

class TestPartition(unittest.TestCase):
    def test_partition(self):
        # Test case 1
        edges1 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 5), (4, 5)]
        g1 = NeighborsGraph(edges=edges1)
        A1, B1, k1_approx = partition(g1)
        print(A1, B1, k1_approx)
        g1_Graph = Graph(6)
        g1_Graph.graph = [  [0, 1, 1, 0, 0, 0],
                            [1, 0, 0, 1, 1, 0],
                            [1, 0, 0, 0, 1, 0],
                            [0, 1, 0, 0, 0, 1],
                            [0, 1, 1, 0, 0, 1],
                            [0, 0, 0, 1, 1, 0]]
        k1 = find_min_k(g1_Graph)
        print(str(k1) + ' vs ' + str(k1_approx))
        self.assertLessEqual(k1, k1_approx)

        # Test case 2
        edges2 = [(0, 1), (0, 2), (1, 2), (2, 3)]
        g2 = NeighborsGraph(edges=edges2)
        A2, B2, k2_approx = partition(g2)
        print(A2, B2, k2_approx)
        g2_Graph = Graph(4)
        g2_Graph.graph = [  [0, 1, 1, 0],
                            [1, 0, 1, 0],
                            [1, 1, 0, 1],
                            [0, 0, 1, 0]]
        k2 = find_min_k(g2_Graph)
        print(str(k2) + ' vs ' + str(k2_approx))
        self.assertLessEqual(k2, k2_approx)

        # Test case 3
        edges3 = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]
        g3 = NeighborsGraph(edges=edges3)
        A3, B3, k3_approx = partition(g3)
        print(A3, B3, k3_approx)
        g3_Graph = Graph(5)
        g3_Graph.graph = [  [0, 1, 1, 0, 0],
                            [1, 0, 1, 0, 0],
                            [1, 1, 0, 1, 0],
                            [0, 0, 1, 0, 1],
                            [0, 0, 0, 1, 0]]
        k3 = find_min_k(g3_Graph)
        print(str(k3) + ' vs ' + str(k3_approx))
        self.assertLessEqual(k3, k3_approx)

        # Test case 4
        edges4 = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5), (5, 6), (5, 7), (6, 7), (7, 8), (8, 9), (8, 10), (9, 10)]
        g4 = NeighborsGraph(edges=edges4)
        A4, B4, k4_approx = partition(g4)
        print(A4, B4, k4_approx)
        g4_Graph = Graph(11)
        g4_Graph.graph = [  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]
        k4 = find_min_k(g4_Graph)
        print(str(k4) + ' vs ' + str(k4_approx))
        self.assertLessEqual(k4, k4_approx)

if __name__ == '__main__':
    unittest.main()