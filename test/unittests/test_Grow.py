import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe import enums
from gwlfe.Input.WaterBudget import Grow


class TestGrow(VariableUnitTest):

    def test_Grow(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Grow.Grow_f(z.Grow_0),
            Grow.Grow(z.Grow_0) == enums.GROWING_SEASON, decimal=7)
