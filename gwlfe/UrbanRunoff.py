import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from UrbanQTotal_1 import UrbanQTotal_1


@memoize
def UrbanRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                  ISRR, ISRA):
    result = np.zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbanqtotal_1 = UrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                  ISRR, ISRA)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i] += urbanqtotal_1[Y][i][j]
                else:
                    pass
    return result


def UrbanRunoff_2():
    pass
