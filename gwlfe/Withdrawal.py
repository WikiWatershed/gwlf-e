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


def AvWithdrawal(NYrs, Withdrawal):
    result = np.zeros((12,))
    for Y in range(NYrs):
        for i in range(12):
            result[i] += Withdrawal[Y][i] / NYrs
    return result


def AvWithdrawal_2():
    pass
