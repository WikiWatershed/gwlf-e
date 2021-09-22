import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import AgRunoff


class TestAgRunoff(VariableUnitTest):

    # @skip("not ready")
    def test_AgRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AgRunoff.AgRunoff_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb,
                                z.Grow_0, z.Landuse, z.Area),
            AgRunoff.AgRunoff(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb,
                              z.Grow_0, z.Landuse, z.Area), decimal=7)
