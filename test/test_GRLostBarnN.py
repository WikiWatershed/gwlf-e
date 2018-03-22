import unittest
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import GRLostBarnN


class TestGRLostBarnN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()
        self.mock_GRInitBarnN = np.load("GRInitBarnN.npy")
        self.mock_LossFactAdj = np.load("LossFactAdj.npy")

    @patch('gwlfe.LossFactAdj.LossFactAdj')
    @patch('gwlfe.GRInitBarnN.GRInitBarnN')
    @patch('gwlfe.GRAppManN.GRAppManN')
    @patch('gwlfe.GrazingN.GrazingN')
    def test_GRLostBarnN(self,LossFactAdj_patch,GRInitBarnN_patch,GRAppManN_patch,GrazingN_patch):
        LossFactAdj_patch.return_value = np.load("LossFactAdj.npy")
        GRInitBarnN_patch.return_value = np.load("GRInitBarnN.npy")
        GRAppManN_patch.return_value = np.load("GRAppManN.npy")
        GrazingN_patch.return_value = np.load("GrazingN.npy")
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLostBarnN.GRLostBarnN(z.NYrs, z.InitGrN, z.GRPctManApp, z.PctGrazingN, z.GRBarnNRate, z.Precipitation, z.DaysMonth,
                                               z.AWMSNgPct,
                                               z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            GRLostBarnN.GRLostBarnN_2(z.NYrs, z.InitGrN, z.GRPctManApp, z.PctGrazingN, z.GRBarnNRate, z.Precipitation, z.DaysMonth,
                                               z.AWMSNgPct,
                                               z.GrAWMSCoeffN, z.RunContPct), decimal=7)