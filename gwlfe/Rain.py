import numpy as np
from Timer import time_function


def Rain(NYrs, DaysMonth, Temp, Prec):
    result = np.zeros((NYrs, 12, 31))

    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = 0
                if Temp[Y][i][j] <= 0:
                    pass
                else:
                    result[Y][i][j] = Prec[Y][i][j]
    return result


def Rain_2():
    pass
