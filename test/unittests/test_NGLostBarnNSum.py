import numpy as np
from VariableUnittest import VariableUnitTest
from gwlfe.AFOS.nonGrazingAnimals.Losses import NGLostBarnNSum
from unittest import skip


class TestNGLostBarnNSum(VariableUnitTest):
    @skip('Not Ready Yet.')
    def test_NGLostBarnNSum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostBarnNSum.NGLostBarnNSum_f(),
            NGLostBarnNSum.NGLostBarnNSum(), decimal=7)