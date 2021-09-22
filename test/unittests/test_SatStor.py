import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import SatStor


class TestSatStor(VariableUnitTest):

    def test_SatStor(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SatStor.SatStor_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                              z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                              z.RecessionCoef, z.SeepCoef),
            SatStor.SatStor(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                            z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                            z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                            z.RecessionCoef, z.SeepCoef), decimal=7)
