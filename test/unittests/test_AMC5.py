import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe import DailyArrayConverter
from gwlfe.Input.WaterBudget import AMC5


class TestAMC5(VariableUnitTest):

    def test_AMC5(self):
        z = self.z

        yesterday_amc5 = DailyArrayConverter.ymd_to_daily(
            AMC5.AMC5_yesterday(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0), z.DaysMonth)
        amc5 = DailyArrayConverter.ymd_to_daily(
            AMC5.AMC5(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0), z.DaysMonth)
        np.testing.assert_array_almost_equal(
            yesterday_amc5[1:], amc5[:-1], decimal=7)
