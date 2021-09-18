import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import CNumPervReten


class TestCNumPervReten(VariableUnitTest):

    def test_CNumPervReten(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNumPervReten.CNumPervReten_f(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur,
                                          z.NUrb, z.CNP_0, z.Grow_0),
            CNumPervReten.CNumPervReten(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur, z.NUrb,
                                        z.CNP_0, z.Grow_0), decimal=7)
