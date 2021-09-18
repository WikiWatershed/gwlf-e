import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import ET


class TestET(VariableUnitTest):

    def test_DailyETPart1(self):
        z = self.z
        np.testing.assert_array_almost_equal(ET.DailyET_f(z.Temp, z.KV, z.PcntET, z.DayHrs),
                                             ET.DailyET(z.NYrs, z.DaysMonth, z.Temp, z.DayHrs, z.KV, z.PcntET,
                                                        z.ETFlag), decimal=7)
