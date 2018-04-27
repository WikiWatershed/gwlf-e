import numpy as np
from Timer import time_function
from Melt_1 import Melt_1
from Rain import Rain
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


def Water_2():
    pass
