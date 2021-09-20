import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.Stream import FilterEff


class TestFilterEff(VariableUnitTest):

    def test_FilterEff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            FilterEff.FilterEff_f(z.FilterWidth),
            FilterEff.FilterEff(z.FilterWidth), decimal=7)
