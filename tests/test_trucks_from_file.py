import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import *

class Test_trucks_from_file(unittest.TestCase):

    def test_trucks0(self):
        camions = trucks_from_file("input/trucks.0.in")
        self.assertEqual(camions, [[2000000, 200000], [6000000, 900000]])

if __name__ == '__main__':
    unittest.main()