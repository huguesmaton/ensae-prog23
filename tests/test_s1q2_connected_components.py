# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_GraphCC(unittest.TestCase):

    #Tests implémentés par le professeur
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})})

    def test_network1(self):
        g = graph_from_file("input/network.01.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})})

    
    #Tests ajoutés
    def test_network2(self):
        g = graph_from_file("input/network.02.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4}), frozenset({5}), frozenset({6}), frozenset({7}), frozenset({8}), frozenset({9}), frozenset({10})})

    def test_network5(self):
        g = graph_from_file("input/network.05.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4})})


if __name__ == '__main__':
    unittest.main()
