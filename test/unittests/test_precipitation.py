import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import Precipitation


class TestPrecipitation(VariableUnitTest):

    def test_Precipitation(self):
        z = self.z
        temp_f = Precipitation.Precipitation_f(z.Prec)
        temp = Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec)
        np.testing.assert_array_almost_equal(Precipitation.Precipitation_f(z.Prec),
                                             Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec), decimal=7)
