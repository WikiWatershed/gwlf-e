import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import WashImperv


class TestWashImperv(VariableUnitTest):

    def test_WashImperv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            WashImperv.WashImperv_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNI_0, z.AntMoist_0, z.Grow_0,
                                    z.NRur, z.NUrb),
            WashImperv.WashImperv(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNI_0, z.AntMoist_0, z.Grow_0,
                                  z.NRur, z.NUrb), decimal=7)
