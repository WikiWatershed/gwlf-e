import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import InitSnow


class TestInitSnow(VariableUnitTest):

    def test_InitSnow(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            InitSnow.InitSnow_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec),
            InitSnow.InitSnow(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec), decimal=7)
