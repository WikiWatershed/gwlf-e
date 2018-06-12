import numpy as np
# from Timer import time_function
from Melt_1 import Melt_1, Melt_1_2
from Rain import Rain, Rain_2
from Memoization import memoize

@memoize
def Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    result = np.zeros((NYrs, 12, 31))
    melt_1 = Melt_1(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    rain = Rain(NYrs, DaysMonth, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = rain[Y][i][j] + melt_1[Y][i][j]
    return result

@memoize
def Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    melt_1 = Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    rain = Rain_2(Temp, Prec)
    return rain + melt_1