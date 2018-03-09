import unittest
import numpy as np
from gwlfe import Parser
from gwlfe import Withdrawal


class TestWithdrawal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_Withdrawal(self):
        z = self.z
        np.testing.assert_array_almost_equal(Withdrawal.Withdrawal_2(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal),
                                             Withdrawal.Withdrawal(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal),
                                             decimal=7)

    def test_AvWithdrawal(self):
        z = self.z
        z.Withdrawal = Withdrawal.Withdrawal(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal)
        np.testing.assert_array_almost_equal(Withdrawal.AvWithdrawal_2(z.NYrs, z.Withdrawal),
                                             Withdrawal.AvWithdrawal(z.NYrs, z.Withdrawal), decimal=7)
