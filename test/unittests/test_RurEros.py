import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Erosion import RurEros


class TestRurEros(VariableUnitTest):

    def test_elementwise_RurEros(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load(self.basepath + "/RurEros.npy"),
            RurEros.RurEros_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                              z.Area), decimal=7)

    def test_RurEros(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RurEros.RurEros_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                              z.Area),
            RurEros.RurEros(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                            z.Area), decimal=7)
