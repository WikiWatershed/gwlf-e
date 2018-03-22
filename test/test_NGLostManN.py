import unittest
from mock import patch
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe import NGLostManN


class TestNGLostManN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()
        self.mock_LossFactAdj = np.load("LossFactAdj.npy")

    @skip("not ready")
    @patch('gwlfe.LossFactAdj.LossFactAdj')
    def test_NGLostManN(self, test_patch):
        z = self.z
        test_patch.return_value = np.load("LossFactAdj.npy")
        np.testing.assert_array_almost_equal(
            NGLostManN.NGLostManN(z.NYrs, z.NGAppManN, z.NGAppNRate, z.Precipitation, z.DaysMonth,
                                  z.NGPctSoilIncRate),
            NGLostManN.NGLostManN_2(z.NYrs, z.NGAppManN, z.NGAppNRate, z.Precipitation, z.DaysMonth,
                                    z.NGPctSoilIncRate), decimal=7)
