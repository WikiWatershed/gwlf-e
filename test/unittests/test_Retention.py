import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import Retention


class TestRetention(VariableUnitTest):

    def test_Retention(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Retention.Retention_f(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                                  z.Grow_0),
            Retention.Retention(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                                z.Grow_0), decimal=7)
