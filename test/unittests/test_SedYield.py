import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.Loading import SedYield


class TestSedYield(VariableUnitTest):

    def test_elementwise_SedYield(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load(self.basepath + "/SedYield.npy"),
            SedYield.SedYield(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C,
                              z.P, z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention,
                              z.PctAreaInfil, z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0), decimal=7)

    def test_SedYield(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SedYield.SedYield_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C,
                                z.P, z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention,
                                z.PctAreaInfil, z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0),
            SedYield.SedYield(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C,
                              z.P, z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention,
                              z.PctAreaInfil, z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0), decimal=7)
