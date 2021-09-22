import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import RurQRunoff


class TestRurQRunoff(VariableUnitTest):
    def test_RurQRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RurQRunoff.RurQRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb,
                                    z.CN, z.Grow_0),
            np.swapaxes(
                RurQRunoff.RurQRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb,
                                      z.CN, z.Grow_0), 1, 2)[:, :, :z.NRur], decimal=7)
