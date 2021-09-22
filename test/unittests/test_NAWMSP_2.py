from unittest import skip

import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.AgAnimal import NAWMSP_2


class TestNAWMSP_2(VariableUnitTest):
    @skip('Not Ready Yet.')
    def test_NAWMSP_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAWMSP_2.NAWMSP_2_f(),
            NAWMSP_2.NAWMSP_2(), decimal=7)
