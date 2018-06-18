import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe.Input.WaterBudget import ET_1
from gwlfe import Parser


class TestET_f(VariableUnitTest):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_ET_f(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            ET_1.ET_1_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET,
                        z.DayHrs, z.MaxWaterCap),
            ET_1.ET_1(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                      z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET,
                      z.DayHrs, z.MaxWaterCap, z.ETFlag), decimal=7)
