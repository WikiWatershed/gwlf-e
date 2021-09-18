import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Erosion import LuErosion


class TestLuErosion(VariableUnitTest):

    # @skip("not ready")
    def test_LuErosion(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LuErosion.LuErosion_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.Acoef, z.KF, z.LS,
                                  z.C, z.P, z.Area),
            LuErosion.LuErosion(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Acoef, z.KF, z.LS,
                                z.C, z.P, z.Area), decimal=7)
