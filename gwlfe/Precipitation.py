import numpy as np
from Timer import time_function
from Memoization import memoize


@memoize
def Precipitation(NYrs, DaysMonth, Prec):
    Precipitation = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                Precipitation[Y][i] = Precipitation[Y][i] + Prec[Y][i][j]
    return Precipitation


def Precipitation_2(Prec):
    fastPrecipitation = np.sum(Prec, axis=(2))
    return fastPrecipitation


def AvPrecipitation(NYrs, Precipitation):
    result = np.zeros((12,))
    for Y in range(NYrs):
        for i in range(12):
            result[i] += Precipitation[Y][i] / NYrs
    return result


def AvPrecipitation_2(Precipitation):
    return np.average(Precipitation, axis=(0))
