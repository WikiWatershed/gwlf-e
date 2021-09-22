import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import WashPerv


class TestPervAccum(VariableUnitTest):

    def test_PervAccum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            WashPerv.WashPerv_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNP_0, z.AntMoist_0, z.Grow_0,
                                z.NRur, z.NUrb),
            WashPerv.WashPerv(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNP_0, z.AntMoist_0, z.Grow_0,
                              z.NRur, z.NUrb), decimal=7)
