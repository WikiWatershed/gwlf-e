import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import CNumImpervReten


class TestCNumImpervReten(VariableUnitTest):

    def test_CNumImpervReten(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNumImpervReten.CNumImpervReten_f(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur,
                                              z.NUrb, z.CNI_0, z.Grow_0),
            CNumImpervReten.CNumImpervReten(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur,
                                            z.NUrb, z.CNI_0, z.Grow_0), decimal=7)
