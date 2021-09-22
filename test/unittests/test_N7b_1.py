from unittest import skip

import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.AvAnimalNSum.N7b_1 import N7b_1


class TestN7b_1(VariableUnitTest):
    @skip("not ready")
    def test_N7b_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            N7b_1.N7b_1_2(),
            N7b_1.N7b_1(), decimal=7)
