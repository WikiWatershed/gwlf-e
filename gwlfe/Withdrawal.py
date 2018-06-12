from numpy import repeat
from numpy import reshape
from numpy import zeros


# from Timer import time_function


# @memoize

def Withdrawal(NYrs, StreamWithdrawal, GroundWithdrawal):
    result = zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (result[Y][i] + StreamWithdrawal[i] + GroundWithdrawal[i])
    return result


def Withdrawal_2(NYrs, StreamWithdrawal, GroundWithdrawal):
    return reshape(repeat(StreamWithdrawal + GroundWithdrawal, NYrs), (NYrs, 12))
