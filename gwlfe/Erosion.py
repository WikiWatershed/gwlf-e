from numpy import sum
from numpy import zeros

# from Timer import time_function
from Memoization import memoize
from RurEros import RurEros
from RurEros import RurEros_f
from Water import Water
from Water import Water_f


@memoize
def Erosion(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    result = zeros((NYrs, 12))
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


@memoize
def Erosion_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    rureros = RurEros_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    # return np.sum(np.where((Temp > 0) & (water > 0.01), np.sum(rureros, axis=3), 0), axis=2)
    return sum(sum(rureros, axis=3), axis=2)