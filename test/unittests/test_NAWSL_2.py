from unittest import skip

import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.AgAnimal import NAWSL_2


class TestNAWSL_2(VariableUnitTest):
    @skip('Not Ready Yet.')
    def test_NAWSL_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAWSL_2.NAWSL_2_f(),
            NAWSL_2.NAWSL_2(), decimal=7)
