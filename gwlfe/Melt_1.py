import numpy as np
from Timer import time_function
from InitSnow import InitSnow
from InitSnowYesterday import InitSnowYesterday
from Melt import Melt, Melt_3
from numba import jit
from Memoization import memoize

@memoize
def Melt_1(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    result = np.zeros((NYrs, 12, 31))
    init_snow = InitSnow(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    init_snow_yesterday = InitSnow_0
    melt = Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and init_snow_yesterday > 0.001 and melt[Y][i][j] > init_snow_yesterday:
                    result[Y][i][j] = init_snow_yesterday
                else:
                    result[Y][i][j] = melt[Y][i][j]
                init_snow_yesterday = init_snow[Y][i][j]
    return result

# @time_function
@jit(cache=True)
def Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    # result = np.zeros((NYrs, 12, 31))
    init_snow_yesterday = InitSnowYesterday(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt_3(NYrs, DaysMonth, Temp, InitSnow_0, Prec)
    melt[np.where((Temp> 0) & (init_snow_yesterday > 0.001) & (melt > init_snow_yesterday))] = init_snow_yesterday[np.where((Temp> 0) & (init_snow_yesterday > 0.001) & (melt > init_snow_yesterday))]
    return melt
