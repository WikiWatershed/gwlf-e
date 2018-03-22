import unittest
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import NGLostBarnN


class TestNGLostBarnN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @patch('gwlfe.LossFactAdj.LossFactAdj')
    def test_NGLostBarnN(self,test_patch):
        z = self.z
        test_patch.return_value = np.load("LossFactAdj.npy")
        np.testing.assert_array_almost_equal(
            NGLostBarnN.NGLostBarnN(z.NYrs, z.NGInitBarnN, z.NGBarnNRate, z.Precipitation, z.DaysMonth, z.AWMSNgPct,
                                    z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            NGLostBarnN.NGLostBarnN_2(z.NYrs, z.NGInitBarnN, z.NGBarnNRate, z.Precipitation, z.DaysMonth, z.AWMSNgPct,
                                      z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN), decimal=7)
