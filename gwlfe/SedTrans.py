import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from Water import Water_2
from AdjQTotal import AdjQTotal
from AdjQTotal import AdjQTotal_2

@memoize
def SedTrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
             ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = np.zeros((NYrs, 12))  # These used to be (NYrs,16) but it looks like a mistake
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjqtotal = AdjQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                          Imper,
                          ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i] = result[Y][i] + adjqtotal[Y][i][j] ** 1.67
                else:
                    result[Y][i] = result[Y][i]
    return result

@memoize
def SedTrans_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
               ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjqtotal = AdjQTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                          Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)

    return np.sum(np.where(np.logical_and(Temp > 0, water > 0.01), adjqtotal ** 1.67, 0), axis=2)
