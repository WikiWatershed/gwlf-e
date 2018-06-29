import numpy as np
from VariableUnittest import VariableUnitTest
from gwlfe.BMPs.AgAnimal import NAWMSL_2
from unittest import skip


class TestNAWMSL_2(VariableUnitTest):
    @skip('Not Ready Yet.')
    def test_NAWMSL_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAWMSL_2.NAWMSL_2_f(),
            NAWMSL_2.NAWMSL_2(), decimal=7)