from unittest import skip

import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import UnSatStorCarryover


class TestUnSatStorCarryover(VariableUnitTest):
    @skip("not ready")
    def test_UnSatStorCarryover(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UnSatStorCarryover.UnSatStorCarryover_2(),
            UnSatStorCarryover.UnSatStorCarryover(), decimal=7)
