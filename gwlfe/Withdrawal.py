import numpy as np
# from Timer import time_function
from Memoization import memoize


# @memoize

def Withdrawal(NYrs, StreamWithdrawal, GroundWithdrawal):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (result[Y][i] + StreamWithdrawal[i] + GroundWithdrawal[i])
    return result


def Withdrawal_2(NYrs, StreamWithdrawal, GroundWithdrawal):
    return np.reshape(np.repeat(StreamWithdrawal + GroundWithdrawal, NYrs), (NYrs, 12))
