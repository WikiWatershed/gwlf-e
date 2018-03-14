import numpy as np
from Timer import time_function


def Withdrawal(NYrs, StreamWithdrawal, GroundWithdrawal):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (result[Y][i] + StreamWithdrawal[i] + GroundWithdrawal[i])
    return result


def Withdrawal_2(NYrs, StreamWithdrawal, GroundWithdrawal):
    # Appears the same for every year by month
    result = np.add(StreamWithdrawal, GroundWithdrawal)
    return np.repeat(result[:, None], NYrs, axis=1).T


def AvWithdrawal(NYrs, Withdrawal):
    result = np.zeros((12,))
    for Y in range(NYrs):
        for i in range(12):
            result[i] += Withdrawal[Y][i] / NYrs
    return result


def AvWithdrawal_2(StreamWithdrawal, GroundWithdrawal):
    # I am not sure this is necessary as every year will be equal based on the definition of Withdraw
    return np.add(StreamWithdrawal, GroundWithdrawal)
