import numpy as np
from Timer import time_function
from DailyArrayConverter import get_value_for_yesterday
from InitSnow import InitSnow


def Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec):
    result = np.zeros((NYrs, 12, 31))
    init_snow = InitSnow(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and get_value_for_yesterday(init_snow, InitSnow_0, Y, i, j, NYrs,
                                                                 DaysMonth) > 0.001:
                    result[Y][i][j] = 0.45 * Temp[Y][i][j]
                else:
                    result[Y][i][j] = 0
    return result


def Melt_2():
    pass
