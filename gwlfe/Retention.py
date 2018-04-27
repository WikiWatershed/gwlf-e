import numpy as np
from Timer import time_function
from NLU import NLU
from CNum import CNum
from Water import Water
from Memoization import memoize


@memoize
def Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu))
    c_num = CNum(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        if CN[l] > 0:  # TODO:CN is set to zero in datamodel
                            result[Y][i][j][l] = 2540 / c_num[Y][i][j][l] - 25.4
                            if result[Y][i][j][l] < 0:
                                result[Y][i][j][l] = 0
    return result


def Retention_2():
    pass
