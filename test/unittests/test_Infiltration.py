import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import Infiltration


class TestInfiltration(VariableUnitTest):

    def test_Infiltration_ground_truth(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load(self.basepath + "/Infiltration.npy"),
            Infiltration.Infiltration(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                      z.CNI_0, z.AntMoist_0,
                                      z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN), decimal=7)

    # @skip('Not Ready Yet.')
    def test_Infiltration(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Infiltration.Infiltration_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                        z.CNI_0, z.AntMoist_0,
                                        z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN),
            Infiltration.Infiltration(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                      z.CNI_0, z.AntMoist_0,
                                      z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN), decimal=7)
