import numpy as np
# from Timer import time_function
from Memoization import memoize
from Water import Water
from UrbAreaTotal import UrbAreaTotal
from UrbAreaTotal import UrbAreaTotal_2
from UrbanRunoff import UrbanRunoff
from UrbanRunoff import UrbanRunoff_2


@memoize
def UrbRunoffLiter(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                   ISRR, ISRA):
    result = np.zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
    urbanrunoff = UrbanRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0, Imper,
                              ISRR, ISRA)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i] = (urbanrunoff[Y][i] / 100) * urbareatotal * 10000 * 1000
                else:
                    pass
    return result


@memoize
def UrbRunoffLiter_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                     CNP_0, Imper, ISRR, ISRA):
    urbareatotal = UrbAreaTotal_2(NRur, NUrb, Area)
    urbanrunoff = UrbanRunoff_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0, Imper, ISRR, ISRA)
    return urbanrunoff / 100 * urbareatotal * 10000 * 1000
