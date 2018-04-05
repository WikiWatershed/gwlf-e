import numpy as np
from Timer import time_function
from InitSnow import InitSnow
from Rain import Rain
from Melt_1 import Melt_1


def Erosiv(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef):
    result = np.zeros((NYrs, 12, 31))
    init_snow = InitSnow(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    init_snow_yesterday = InitSnow_0
    rain = Rain(NYrs, DaysMonth, Temp, Prec)
    melt_1 = Melt_1(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0:
                    if (init_snow_yesterday > 0.001):
                        if rain[Y][i][j] > 0 and init_snow_yesterday - melt_1[Y][i][j] < 0.001:
                            result[Y][i][j] = 6.46 * Acoef[i] * rain[Y][i][j] ** 1.81
                    else:
                        if rain[Y][i][j] > 0 and init_snow_yesterday < 0.001:
                            result[Y][i][j] = 6.46 * Acoef[i] * rain[Y][i][j] ** 1.81
                init_snow_yesterday = init_snow[Y][i][j]
    return result


def Erosiv_2():
    pass
