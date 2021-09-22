import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import CNumPerv


class TestCNumPerv(VariableUnitTest):

    # @skip("not ready")
    def test_CNumPerv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNumPerv.CNumPerv_f(z.NYrs, z.DaysMonth, z.Temp, z.NRur, z.NUrb, z.CNP_0, z.InitSnow_0, z.Prec, z.Grow_0,
                                z.AntMoist_0),
            CNumPerv.CNumPerv(z.NYrs, z.DaysMonth, z.Temp, z.NRur, z.NUrb, z.CNP_0, z.InitSnow_0, z.Prec, z.Grow_0,
                              z.AntMoist_0), decimal=7)
