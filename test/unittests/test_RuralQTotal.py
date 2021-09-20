import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Discharge import RuralQTotal


class TestRuralQTotal(VariableUnitTest):

    def test_RuralQTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RuralQTotal.RuralQTotal_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.NUrb,
                                      z.AntMoist_0, z.Grow_0, z.Area),
            RuralQTotal.RuralQTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.NUrb,
                                    z.AntMoist_0, z.Grow_0, z.Area), decimal=7)
