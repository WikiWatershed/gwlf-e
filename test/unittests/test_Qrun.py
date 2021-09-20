import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import Qrun


class TestQrun(VariableUnitTest):
    def test_Qrun(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Qrun.Qrun_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.CN, z.AntMoist_0,
                        z.Grow_0),
            Qrun.Qrun(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.CN, z.AntMoist_0, z.Grow_0),
            decimal=7)
