import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import QrunI


class TestQRunI(VariableUnitTest):

    def test_QRunI(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            QrunI.QrunI_f(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNI_0, z.AntMoist_0,
                          z.Grow_0),
            QrunI.QrunI(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNI_0, z.AntMoist_0,
                        z.Grow_0), decimal=7)
