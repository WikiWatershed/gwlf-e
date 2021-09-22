import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import GrowFactor


class TestGrowFactor(VariableUnitTest):

    def test_GrowFactor(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrowFactor.GrowFactor_f(z.Grow_0),
            GrowFactor.GrowFactor(z.Grow_0), decimal=7)
