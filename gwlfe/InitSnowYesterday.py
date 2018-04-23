import numpy as np
from Timer import time_function
from numba import jit


@jit(cache=True, nopython = True)
def InitSnowYesterday(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    # result = np.zeros((NYrs, 12, 31))
    result_yesterday = np.zeros((NYrs, 12, 31))
    yesterday = InitSnow_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result_yesterday[Y][i][j] = yesterday
                if Temp[Y][i][j] <= 0:
                    snow = yesterday + Prec[Y][i][j]
                else:
                    if yesterday > 0.001:
                        snow = max(yesterday - 0.45 * Temp[Y][i][j], 0)
                    else:
                        snow = yesterday
                yesterday = snow
    return result_yesterday
