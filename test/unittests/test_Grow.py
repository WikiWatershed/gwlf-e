import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe.Input.WaterBudget import Grow
from gwlfe import enums


class TestGrow(VariableUnitTest):

    def test_Grow(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Grow.Grow_f(z.Grow_0),
            Grow.Grow(z.Grow_0) == enums.GROWING_SEASON, decimal=7)
