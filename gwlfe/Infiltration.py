import numpy as np
from Timer import time_function
from QTotal import QTotal
from Water import Water
from Memoization import memoize
from QTotal import QTotal_2
from Water import Water_2

@time_function
# @memoize
def Infiltration(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                 ISRR, ISRA, CN):
    result = np.zeros((NYrs, 12, 31))
    qtotal = QTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                    ISRR, ISRA, CN)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if qtotal[Y][i][j] <= water[Y][i][j]:
                    result[Y][i][j] = water[Y][i][j] - qtotal[Y][i][j]
    return result

@time_function
def Infiltration_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                 ISRR, ISRA, CN):
    result = np.zeros((NYrs, 12, 31))
    qtotal = QTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                    ISRR, ISRA, CN)
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    result[np.where(qtotal < water)] = water[np.where(qtotal < water)] - qtotal[np.where(qtotal < water)]
    return result