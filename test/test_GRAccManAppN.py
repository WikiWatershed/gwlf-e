import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe import GRAccManAppN


class TestGRAccManAppN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()
        self.mock_GrazingN = np.load("GrazingN.npy")

    @skip("not ready")
    def test_GRAccManAppN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRAccManAppN.GRAccManAppN(z.InitGrN, z.GRPctManApp, self.mock_GrazingN),
            GRAccManAppN.GRAccManAppN_2(z.InitGrN, z.GRPctManApp, self.mock_GrazingN), decimal=7)