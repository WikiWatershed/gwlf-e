import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import DailyFlow


class TestDailyFlow(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_DailyFlow(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            DailyFlow.DailyFlow_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0,
                                  z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.Qretention, z.PctAreaInfil, z.n25b, z.UnsatStor_0, z.KV, z.PcntET,
                                  z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef),
            DailyFlow.DailyFlow(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0,
                                  z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.Qretention, z.PctAreaInfil, z.n25b, z.UnsatStor_0, z.KV, z.PcntET,
                                  z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef), decimal=7)