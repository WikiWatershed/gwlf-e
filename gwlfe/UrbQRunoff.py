import numpy as np
from Timer import time_function
from Memoization import memoize
from NLU import NLU
from Water import Water
from QrunI import QrunI
from QrunP import QrunP
from LU import LU


@memoize
def UrbQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0, AntMoist_0, Grow, Imper, ISRR, ISRA):
    result = np.zeros((NYrs, 16, 12))
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    qruni = QrunI(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow)
    qrunp = QrunP(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow)
    lu = LU(NRur, NUrb)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(nlu):
                result[Y, l, i] = 0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            result[Y][l][i] += (qruni[Y][i][j][l] * (
                                        Imper[l] * (1 - ISRR[lu[l]]) * (1 - ISRA[lu[l]]))
                                                   + qrunp[Y][i][j][l] * (
                                                           1 - (Imper[l] * (1 - ISRR[lu[l]]) * (
                                                               1 - ISRA[lu[l]]))))

                else:
                    pass
    return result


def UrbQRunoff_2():
    pass
