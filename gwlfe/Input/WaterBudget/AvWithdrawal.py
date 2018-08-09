from numpy import sum
from numpy import zeros

from gwlfe.Input.WaterBudget.Withdrawal import Withdrawal
from gwlfe.Input.WaterBudget.Withdrawal import Withdrawal_f
from gwlfe.Memoization import memoize


def AvWithdrawal(NYrs, StreamWithdrawal, GroundWithdrawal):
    result = zeros(12)
    withdrawal = Withdrawal(NYrs, StreamWithdrawal, GroundWithdrawal)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += withdrawal[Y][i] / NYrs
    return result


@memoize
def AvWithdrawal_f(NYrs, StreamWithdrawal, GroundWithdrawal):
    return sum(Withdrawal_f(NYrs, StreamWithdrawal, GroundWithdrawal), axis=0) / NYrs
