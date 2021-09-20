import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Discharge import AgQTotal


class TestAgQTotal(VariableUnitTest):

    def test_AgQTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AgQTotal.AgQTotal_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb,
                                z.Grow_0, z.Landuse, z.Area),
            AgQTotal.AgQTotal(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb,
                              z.Grow_0, z.Landuse, z.Area), decimal=7)
