import numpy as np
from Timer import time_function


def Withdrawal(NYrs, StreamWithdrawal, GroundWithdrawal):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (result[Y][i] + StreamWithdrawal[i] + GroundWithdrawal[i])
    return result


def Withdrawal_2():
    pass
