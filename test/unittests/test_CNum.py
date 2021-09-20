import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import CNum


class TestCNum(VariableUnitTest):

    def test_elementwise_CNum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load(self.basepath + "/CNum.npy"),
            CNum.CNum(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.CN, z.NRur, z.NUrb,
                      z.Grow_0), decimal=7)

    def test_CNum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNum.CNum(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.CN, z.NRur, z.NUrb, z.Grow_0),
            CNum.CNum_f(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.CN, z.NRur, z.NUrb,
                        z.Grow_0), decimal=7)
