import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Erosion import Erosiv


class TestErosiv(VariableUnitTest):

    def test_elementwise_Erosiv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load(self.basepath + "/Erosiv.npy"),
            Erosiv.Erosiv(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef), decimal=7)

    def test_Erosiv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Erosiv.Erosiv_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef),
            Erosiv.Erosiv(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef), decimal=20)
