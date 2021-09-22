import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import Melt


class TestMelt(VariableUnitTest):

    def test_Melt(self):
        z = self.z
        test = Melt.Melt(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec)
        test1 = Melt.Melt_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec)
        np.testing.assert_array_almost_equal(
            Melt.Melt(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec),
            Melt.Melt_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec), decimal=7)
