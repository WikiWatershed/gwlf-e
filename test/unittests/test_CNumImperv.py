import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import CNumImperv


class TestCNumImperv(VariableUnitTest):

    def test_CNumImperv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNumImperv.CNumImperv_f(z.NYrs, z.NRur, z.NUrb, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNI_0,
                                    z.Grow_0, z.AntMoist_0),
            CNumImperv.CNumImperv(z.NYrs, z.NRur, z.NUrb, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNI_0, z.Grow_0,
                                  z.AntMoist_0), decimal=7)
