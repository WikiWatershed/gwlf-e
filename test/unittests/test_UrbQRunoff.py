import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import UrbQRunoff


class TestUrbQRunoff(VariableUnitTest):

    def test_UrbQRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbQRunoff.UrbQRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                                    z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA),
            np.swapaxes(
                UrbQRunoff.UrbQRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0,
                                      z.CNP_0,
                                      z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA), 1, 2)[:, :, z.NRur:]
            , decimal=7)
