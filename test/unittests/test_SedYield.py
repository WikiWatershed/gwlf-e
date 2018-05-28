import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import SedYield


class TestSedYield(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_SedYield(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SedYield.SedYield_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C,
                                z.P, z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention,
                                z.PctAreaInfil, z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0),
            SedYield.SedYield(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C,
                              z.P, z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention,
                              z.PctAreaInfil, z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0), decimal=7)
