import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Erosion import Erosion


class TestErosion(VariableUnitTest):

    # def test_elementwise_Erosion(self):
    #     z = self.z
    #     np.testing.assert_array_almost_equal(
    #         np.load("unittests/Erosion.npy"),
    #         Erosion.Erosion(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
    #                          z.Area), decimal=7)

    def test_Erosion(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Erosion.Erosion_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                              z.Area),
            Erosion.Erosion(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                            z.Area), decimal=7)
