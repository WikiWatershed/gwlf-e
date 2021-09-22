import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import Melt_1


# from gwlfe import MeltPest


class TestMelt_1(VariableUnitTest):

    def test_Melt_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Melt_1.Melt_1_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec),
            Melt_1.Melt_1(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec), decimal=7)
