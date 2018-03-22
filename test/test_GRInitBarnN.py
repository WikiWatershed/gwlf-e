import unittest
import numpy as np
from gwlfe import Parser
from gwlfe import GRInitBarnN


class TestGRInitBarnN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()
        self.mock_GRAppManN = np.load("GRAppManN.npy")
        self.mock_GrazingN = np.load("GrazingN.npy")


    def test_GRInitBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRInitBarnN.GRInitBarnN(self.mock_GRAppManN, z.InitGrN, z.GRPctManApp, self.mock_GrazingN),
            GRInitBarnN.GRInitBarnN_2(self.mock_GRAppManN, z.InitGrN, z.GRPctManApp, self.mock_GrazingN), decimal=7)