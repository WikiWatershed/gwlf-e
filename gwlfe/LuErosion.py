import numpy as np
from Timer import time_function
from Memoization import memoize
from ErosWashoff import ErosWashoff
from ErosWashoff import ErosWashoff_2

def LuErosion(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Acoef, KF, LS,
              C, P, Area):
    result = np.zeros((NYrs, 16))
    eros_washoff = ErosWashoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Acoef, KF, LS,
                               C, P, Area)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(NRur):
                result[Y][l] += eros_washoff[Y][l][i]
    return result

@memoize
def LuErosion_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, Acoef, KF, LS,
                C, P, Area):
    return np.sum(ErosWashoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, Acoef, KF, LS,
                                C, P, Area), axis=2)
