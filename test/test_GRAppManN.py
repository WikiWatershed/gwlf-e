import unittest
import numpy as np
from gwlfe import Parser
from gwlfe import GRAppManN


class TestGrAppManN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_GrAppManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(GRAppManN.GRAppManN(z.GRPctManApp, z.InitGrN),
                                             GRAppManN.GRAppManN_2(z.GRPctManApp, z.InitGrN), decimal=7)