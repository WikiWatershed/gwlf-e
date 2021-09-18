import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Discharge import QTotal


class TestQTotal(VariableUnitTest):

    def test_QTotal_ground_truth(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load(self.basepath + "/QTotal.npy"),
            QTotal.QTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                          z.AntMoist_0,
                          z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN), decimal=7)

    # @skip("not ready")
    def test_QTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            QTotal.QTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                          z.AntMoist_0,
                          z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN),
            QTotal.QTotal_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                            z.AntMoist_0,
                            z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN), decimal=7)
