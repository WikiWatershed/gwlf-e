import numpy as np
from Timer import time_function
from Memoization import memoize
from NLU import NLU
from Water import Water
from Retention import Retention
from Qrun import Qrun


@memoize
def RurQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0):
    result = np.zeros((NYrs, 16, 12))
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    retention = Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0)
    qrun = Qrun(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(nlu):
                result[Y, l, i] = 0.0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        if CN[l] > 0:
                            if water[Y][i][j] >= 0.2 * retention[Y][i][j][l]:
                                result[Y][l][i] += qrun[Y][i][j][l]
                            else:
                                pass
                        else:
                            pass
                else:
                    pass

    return result


def RurQRunoff_2():
    pass
