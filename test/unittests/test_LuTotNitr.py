import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import LuTotNitr


class TestLuTotNitr(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_LuTotNitr(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LuTotNitr.LuTotNitr_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                                  z.Grow_0, z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth,
                                  z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF,
                                  z.LS, z.C, z.P, z.SedNitr, z.Acoef),
            LuTotNitr.LuTotNitr(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                                  z.Grow_0, z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth,
                                  z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF,
                                  z.LS, z.C, z.P, z.SedNitr, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                  z.PctAreaInfil, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth,
                                  z.PctStrmBuf, z.Acoef, z.CNI_0, z.Nqual)[:,:z.NRur], decimal=7)
