from numpy import sum
from numpy import zeros

# from Timer import time_function
from Memoization import memoize
from Withdrawal import Withdrawal
from Withdrawal import Withdrawal_2


def AvWithdrawal(NYrs, StreamWithdrawal, GroundWithdrawal):
    result = zeros(12)
    withdrawal = Withdrawal(NYrs, StreamWithdrawal, GroundWithdrawal)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += withdrawal[Y][i] / NYrs
    return result

@memoize
def AvWithdrawal_2(NYrs, StreamWithdrawal, GroundWithdrawal):
    return sum(Withdrawal_2(NYrs, StreamWithdrawal, GroundWithdrawal), axis=0) / NYrs
