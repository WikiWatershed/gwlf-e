import unittest
from mock import patch
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import GRLostManN


class TestGRLostManN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()
        self.mock_LossFactAdj = np.load("LossFactAdj.npy")
        self.mock_GRAppManN = np.load("GRAppManN.npy")
    @skip("not ready")
    @patch('gwlfe.LossFactAdj.LossFactAdj')
    def test_GRLostManN(self,test_patch):
        z = self.z
        test_patch.return_value = np.load("LossFactAdj.npy")
        np.testing.assert_array_almost_equal(
            GRLostManN.GRLostManN(z.NYrs, self.mock_GRAppManN, z.GRAppNRate, z.Precipitation, z.DaysMonth,
                                  z.GRPctSoilIncRate),
            GRLostManN.GRLostManN_2(z.NYrs, self.mock_GRAppManN, z.GRAppNRate, z.Precipitation, z.DaysMonth,
                                    z.GRPctSoilIncRate), decimal=7)