import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import LuRunoff


class TestLuRunoff(VariableUnitTest):

    def test_LuRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LuRunoff.LuRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                                z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN),
            LuRunoff.LuRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                              z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN), decimal=7)
