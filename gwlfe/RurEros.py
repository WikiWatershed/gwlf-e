import numpy as np
from Timer import time_function
from Erosiv import Erosiv
from Erosiv import Erosiv_2
from Memoization import memoize
from Water import Water
from Water import Water_2

@memoize
def RurEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    result = np.zeros((NYrs, 12, 31, NRur))
    erosiv = Erosiv(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef)
    water = Water(NYrs,DaysMonth,InitSnow_0,Temp,Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        result[Y][i][j][l] = 1.32 * erosiv[Y][i][j] * KF[l] * LS[l] * C[l] * P[l] * Area[l]
    return result

@memoize
def RurEros_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    erosiv = np.reshape(np.repeat(Erosiv_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef), NRur, axis=2),(NYrs, 12, 31, NRur))
    water = np.reshape(np.repeat(Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec),NRur,axis=2),(NYrs, 12, 31, NRur)) #TODO: is there a way to repeating
    resized_temp = np.reshape(np.repeat(Temp,NRur,axis=2),(NYrs, 12, 31, NRur))
    temp = KF * LS * C * P * Area
    return np.where((resized_temp > 0) & (water > 0.01), 1.32 * erosiv * temp[:NRur], 0)
