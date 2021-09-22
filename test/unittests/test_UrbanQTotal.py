import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Discharge import UrbanQTotal


class TestUrbanQTotal(VariableUnitTest):

    def test_UrbanQTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbanQTotal.UrbanQTotal_f(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.Area,
                                      z.CNI_0,
                                      z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA),
            UrbanQTotal.UrbanQTotal(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.Area, z.CNI_0,
                                    z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA), decimal=7)
