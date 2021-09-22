import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import UrbRunoffLiter


class TestUrbanRunoffLiter(VariableUnitTest):

    def test_UrbanRunoffLiter(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbRunoffLiter.UrbRunoffLiter_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area,
                                            z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA),
            UrbRunoffLiter.UrbRunoffLiter(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area,
                                          z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA),
            decimal=7)
