import numpy as np
from Timer import time_function
from numba import jit

from Memoization import memoize

@jit
def Rain_inner(NYrs, DaysMonth, Temp, Prec):
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

@memoize
def Rain(NYrs, DaysMonth, Temp, Prec):
    return Rain_inner(NYrs,DaysMonth,Temp,Prec)

# @time_function
# @jit(cache=True, nopython = True)
def Rain_2(Temp, Prec):
    return np.where(Temp <= 0,0,Prec )