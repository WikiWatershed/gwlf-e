import numpy as np
from Timer import time_function
from DailyArrayConverter import get_value_for_yesterday
from InitSnow import InitSnow, InitSnow_2
from InitSnowYesterday import InitSnowYesterday
#import InitSnow
from numba import jit
from Memoization import memoize

# @memoize
def Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec):
    result = np.zeros((NYrs, 12, 31))
    init_snow = InitSnow(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    init_snow_yesterday = InitSnow_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and init_snow_yesterday > 0.001:
                    result[Y][i][j] = 0.45 * Temp[Y][i][j]
                else:
                    result[Y][i][j] = 0
                init_snow_yesterday = init_snow[Y][i][j]
    return result

def Melt_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec):
    init_snow_yesterday = InitSnowYesterday(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    return np.where((Temp>0) & (init_snow_yesterday > 0.001), 0.45 * Temp, 0)
