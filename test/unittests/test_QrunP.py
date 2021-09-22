import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import QrunP


class TestQrunP(VariableUnitTest):
    def test_QrunP(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            QrunP.QrunP_f(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNP_0, z.AntMoist_0,
                          z.Grow_0),
            QrunP.QrunP(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNP_0, z.AntMoist_0,
                        z.Grow_0), decimal=7)
