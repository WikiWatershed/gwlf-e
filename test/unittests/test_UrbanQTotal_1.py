import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Discharge import UrbanQTotal_1


class TestUrbanQTotal_1(VariableUnitTest):

    def test_UrbanQTotal_1_ground_truth(self):
        z = self.z
        np.testing.assert_array_almost_equal(

            np.load(self.basepath + "/UrbanQTotal_1.npy"),
            UrbanQTotal_1.UrbanQTotal_1(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur,
                                        z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR,
                                        z.ISRA), decimal=7)

    # @skip("not ready")
    def test_UrbanQTotal_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbanQTotal_1.UrbanQTotal_1_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur,
                                          z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR,
                                          z.ISRA),
            UrbanQTotal_1.UrbanQTotal_1(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur,
                                        z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR,
                                        z.ISRA), decimal=7)
