import unittest
import networkx as nx
from networkx.generators.random_graphs import gnp_random_graph
from networkx.convert_matrix import to_numpy_array
import matplotlib.pyplot as plt
import thewalrus
import hafnian


class HafnianTestCase(unittest.TestCase):
    def test_hafnian_four(self):
        """
        Tests hafnian function against four-by-four graphs
        """
        for i in range(10):  # how many tests to perform
            graph = gnp_random_graph(4, 0.5)

            nx.draw(graph)
            plt.show()  # displays graph (cumbersome for large tests)

            adj = to_numpy_array(graph)  # create adjacency matrix
            walrus = thewalrus.hafnian(adj)  # calculate hafnian with Xanadu library
            haf = hafnian.hafnian(adj)  # calculate my hafnian
            self.assertEqual(walrus, haf)  # compare!


class SlowHafnianTestCase(unittest.TestCase):
    def test_slow_hafnian_four(self):
        """
        Tests slow hafnian function against four-by-four graphs
        """
        for i in range(1):  # how many tests to perform
            graph = gnp_random_graph(10, 0.5)

            nx.draw(graph)
            plt.show()  # displays graph (cumbersome for large tests)

            adj = to_numpy_array(graph)  # create adjacency matrix
            walrus = thewalrus.hafnian(adj)  # calculate hafnian with Xanadu library
            haf = hafnian.slow_hafnian(adj)  # calculate my hafnian
            self.assertEqual(walrus, haf)  # compare!


if __name__ == '__main__':
    unittest.main()
