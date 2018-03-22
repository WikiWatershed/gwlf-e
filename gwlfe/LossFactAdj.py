import numpy as np
from Timer import time_function
from Precipitation import Precipitation


def LossFactAdj(NYrs, Prec, DaysMonth):
    result = np.zeros((NYrs, 12))
    precipitation = Precipitation(NYrs,DaysMonth,Prec)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (precipitation[Y][i] / DaysMonth[Y][i]) / 0.3301
    return result


def LossFactAdj_2(NYrs, Prec, DaysMonth):
    precipitation = Precipitation(NYrs,DaysMonth,Prec)
    result = precipitation / DaysMonth / 0.3301
    return result
