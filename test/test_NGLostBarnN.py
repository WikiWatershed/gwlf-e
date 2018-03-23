import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import NGLostBarnN


class TestNGLostBarnN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    @patch('gwlfe.LossFactAdj.LossFactAdj')
    def test_NGLostBarnN(self, test_patch):
        z = self.z
        test_patch.return_value = np.load("LossFactAdj.npy")
        np.testing.assert_array_almost_equal(
            NGLostBarnN.NGLostBarnN(z.NYrs, z.NGInitBarnN, z.NGBarnNRate, z.Precipitation, z.DaysMonth, z.AWMSNgPct,
                                    z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            NGLostBarnN.NGLostBarnN_2(z.NYrs, z.NGInitBarnN, z.NGBarnNRate, z.Precipitation, z.DaysMonth, z.AWMSNgPct,
                                      z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN), decimal=7)

    @skip("not ready")
    def test_AvNGLostBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostBarnN.AvNGLostBarnN_2(),
            NGLostBarnN.AvNGLostBarnN(), decimal=7)

    @skip("not ready")
    def test_AvNGLostBarnNSum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostBarnN.AvNGLostBarnNSum_2(),
            NGLostBarnN.AvNGLostBarnNSum(), decimal=7)

    @skip("not ready")
    def test_NGLostBarnNSum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostBarnN.NGLostBarnNSum_2(),
            NGLostBarnN.NGLostBarnNSum(), decimal=7)
