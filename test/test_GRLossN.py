import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import GRLossN


class TestGRLossN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()
        self.mock_GrazingN = np.load("GrazingN.npy")
        self.mock_LossFactAdj = np.load("LossFactAdj.npy")

    @skip("not ready")
    def test_GRLossN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLossN.GRLossN(z.NYrs, self.mock_GrazingN, z.GRStreamN, z.GrazingNRate,
                            self.mock_LossFactAdj),
            GRLossN.GRLossN_2(z.NYrs, self.mock_GrazingN, z.GRStreamN, z.GrazingNRate,
                              self.mock_LossFactAdj), decimal=7)
