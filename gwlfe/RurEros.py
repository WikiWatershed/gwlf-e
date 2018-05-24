import numpy as np
from Timer import time_function
from Erosiv import Erosiv
from Memoization import memoize

@memoize
def RurEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    result = np.zeros((NYrs, 12, 31, NRur))
    erosiv = Erosiv(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                for l in range(NRur):
                    result[Y][i][j][l] = 1.32 * erosiv[Y][i][j] * KF[l] * LS[l] * C[l] * P[l] * Area[l]
    return result

def RurEros_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    erosiv = np.reshape(np.repeat(Erosiv(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef), NRur, axis=2),(NYrs, 12, 31, NRur))
    temp = KF * LS * C * P * Area
    return 1.32 * erosiv * temp[:NRur]
