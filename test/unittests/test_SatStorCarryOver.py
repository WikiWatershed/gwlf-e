from unittest import skip

import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import SatStorCarryOver


class TestSatStorCarryOver(VariableUnitTest):
    @skip("not ready")
    def test_SatStorCarryOver(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SatStorCarryOver.SatStorCarryOver_2(),
            SatStorCarryOver.SatStorCarryOver(), decimal=7)
