import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Discharge import DailyFlow


class TestDailyFlow(VariableUnitTest):

    def test_DailyFlow(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            DailyFlow.DailyFlow_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                  z.AntMoist_0, z.Grow_0,
                                  z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.Qretention, z.PctAreaInfil, z.n25b,
                                  z.UnsatStor_0, z.KV, z.PcntET,
                                  z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef),
            DailyFlow.DailyFlow(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                z.AntMoist_0, z.Grow_0,
                                z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.Qretention, z.PctAreaInfil, z.n25b,
                                z.UnsatStor_0, z.KV, z.PcntET,
                                z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef), decimal=7)
