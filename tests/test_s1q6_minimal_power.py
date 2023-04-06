# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):

    #Tests implémentés par le professeur
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.min_power(1, 4)[1], 11)
        self.assertEqual(g.min_power(2, 4)[1], 10)

    def test_network1(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.min_power(1, 4)[1], 4)

    
    #Tests ajoutés 
    def test_network3(self):
        g = graph_from_file("input/network.03.in")
        self.assertEqual(g.min_power(4, 2)[1], 4)
        self.assertEqual(g.min_power(1, 4)[1], 10)

    def test_network5(self):
        g = graph_from_file("input/network.05.in")
        self.assertEqual(g.min_power(3, 4)[1], 4)
        self.assertEqual(g.min_power(1, 2)[1], 6)

if __name__ == '__main__':
    unittest.main()
