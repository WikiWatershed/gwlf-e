import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from UrbAreaTotal import UrbAreaTotal
from UrbanRunoff import UrbanRunoff


@memoize
def UrbRunoffLiter(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                  ISRR, ISRA):
    result = np.zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
    urbanrunoff = UrbanRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                  ISRR, ISRA)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i] = (urbanrunoff[Y][i] / 100) * urbareatotal * 10000 * 1000
                else:
                    pass
    return result


def UrbanRunoffLiter_2():
    pass
