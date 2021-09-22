import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import AvWithdrawal


class TestAvWithdrawal(VariableUnitTest):

    def test_AvWithdrawal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvWithdrawal.AvWithdrawal_f(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal),
            AvWithdrawal.AvWithdrawal(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal), decimal=7)
