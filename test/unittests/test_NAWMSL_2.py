from unittest import skip

import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.AgAnimal import NAWMSL_2


class TestNAWMSL_2(VariableUnitTest):
    @skip('Not Ready Yet.')
    def test_NAWMSL_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAWMSL_2.NAWMSL_2_f(),
            NAWMSL_2.NAWMSL_2(), decimal=7)
