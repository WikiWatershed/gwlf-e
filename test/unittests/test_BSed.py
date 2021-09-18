import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Erosion import BSed


class TestBSed(VariableUnitTest):

    def test_BSed(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            BSed.BSed_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b,
                        z.CN),
            BSed.BSed(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                      z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b,
                      z.CN), decimal=7)
