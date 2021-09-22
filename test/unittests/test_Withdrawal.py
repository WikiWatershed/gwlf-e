import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import Withdrawal


class TestWithdrawal(VariableUnitTest):
    def test_Withdrawal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Withdrawal.Withdrawal_f(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal),
            Withdrawal.Withdrawal(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal), decimal=7)
