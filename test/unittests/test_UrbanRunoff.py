import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import UrbanRunoff


class TestUrbanRunoff(VariableUnitTest):

    def test_UrbanRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbanRunoff.UrbanRunoff_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                      z.CNI_0, z.AntMoist_0, z.Grow_0,
                                      z.CNP_0, z.Imper, z.ISRR, z.ISRA),
            UrbanRunoff.UrbanRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                    z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                    z.ISRR, z.ISRA), decimal=7)
