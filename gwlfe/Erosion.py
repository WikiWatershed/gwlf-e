import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from RurEros import RurEros


@memoize
def Erosion(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    result = np.zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    rureros = RurEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                for l in range(NRur):
                    if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                        result[Y][i] = result[Y][i] + rureros[Y][i][j][l]
                    else:
                        pass
    return result


def Erosion_2():
    pass
