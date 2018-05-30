import numpy as np
from Timer import time_function
from Water import Water, Water_2
import copy
from numba import jit
from Memoization import memoize
from numba.pycc import CC

try:
    from AMC5_yesterday_inner_compiled import AMC5_yesterday_inner
except ImportError:
    print("Unable to import compiled AMC5_yesterday_inner, using slower version")
    from AMC5_yesterday_inner import AMC5_yesterday_inner


# AMC5_yesterday returns the same value as yesterday(AMC5) and faster than any other version
@memoize
def AMC5(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0):
    result = np.zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    AMC5 = 0
    AntMoist = copy.deepcopy(AntMoist_0)
    for k in range(5):
        AMC5 += AntMoist[k]
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                AMC5 = AMC5 - AntMoist[4] + water[Y][i][j]
                AntMoist[4] = AntMoist[3]
                AntMoist[3] = AntMoist[2]
                AntMoist[2] = AntMoist[1]
                AntMoist[1] = AntMoist[0]
                AntMoist[0] = water[Y][i][j]

                result[Y][i][j] = AMC5  # TODO: why did this fix the mismatch of amc5?

    return result


# @time_function
# @jit(cache=True)
# def AMC5_2(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0):
#     result = np.zeros((NYrs, 12, 31))
#     water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
#     AMC5 = 0
#     AntMoist = copy.deepcopy(AntMoist_0)
#     AMC5 = np.sum(AntMoist)
#     for Y in range(NYrs):
#         for i in range(12):
#             for j in range(DaysMonth[Y][i]):
#                 AMC5 = AMC5 - AntMoist[4] + water[Y][i][j]
#                 AntMoist[4] = AntMoist[3]
#                 AntMoist[3] = AntMoist[2]
#                 AntMoist[2] = AntMoist[1]
#                 AntMoist[1] = AntMoist[0]
#                 AntMoist[0] = water[Y][i][j]
#
#                 result[Y][i][j] = AMC5  # TODO: why did this fix the mismatch of amc5?
#
#     return result


def AMC5_1(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0):
    result = np.zeros((NYrs, 12, 31))
    AntMoist1 = np.zeros((5,))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    AMC5 = 0
    for k in range(5):
        AMC5 += AntMoist_0[k]
        AntMoist1[k] = AntMoist_0[k]
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = AMC5
                AMC5 = AMC5 - AntMoist1[4] + water[Y][i][j]
                AntMoist1[4] = AntMoist1[3]
                AntMoist1[3] = AntMoist1[2]
                AntMoist1[2] = AntMoist1[1]
                AntMoist1[1] = AntMoist1[0]
                AntMoist1[0] = water[Y][i][j]
    return result


def AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0):
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    return AMC5_yesterday_inner(NYrs, DaysMonth, AntMoist_0, water)
