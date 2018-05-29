import numpy as np
from Timer import time_function
from Memoization import memoize
from Erosion import Erosion
from Erosion import Erosion_2


def AvErosion(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    result = np.zeros(12)
    erosion = Erosion(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += erosion[Y][i] / NYrs
    return result


def AvErosion_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    return np.sum(Erosion_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area), axis=0) / NYrs
