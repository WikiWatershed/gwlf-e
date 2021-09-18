import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import Percolation


class TestPercolation(VariableUnitTest):

    def test_Percolation_ground_truth(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load(self.basepath + "/Percolation.npy"),
            Percolation.Percolation(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                    z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                    z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap), decimal=7)

    def test_Percolation(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Percolation.Percolation_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                      z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                      z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap),
            Percolation.Percolation(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                    z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                    z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap), decimal=7)
