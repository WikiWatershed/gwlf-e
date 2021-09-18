import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Discharge import AdjUrbanQTotal_1


class TestAdjUrbanQTotal_1(VariableUnitTest):

    def test_AdjUrbanQTotal_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AdjUrbanQTotal_1.AdjUrbanQTotal_1_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb,
                                                z.Area,
                                                z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                                                z.Qretention, z.PctAreaInfil),
            AdjUrbanQTotal_1.AdjUrbanQTotal_1(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                              z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                                              z.Qretention, z.PctAreaInfil),
            decimal=7)
