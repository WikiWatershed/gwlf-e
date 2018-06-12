# from Timer import time_function
import math

from Memoization import memoize
from NLU import NLU
from QrunP import QrunP
from QrunP import QrunP_2
from Water import Water
from Water import Water_2
from numpy import zeros
from numpy import exp

try:
    from WashPerv_inner_compiled import WashPerv_inner
except ImportError:
    print("Unable to import compiled WashPerv_inner, using slower version")
    from WashPerv_inner import WashPerv_inner


@memoize
def WashPerv(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNP_0, AntMoist_0, Grow_0, NRur, NUrb):
    pervaccum = zeros(16)
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    qrunp = QrunP(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow_0)
    washperv = zeros((NYrs, 12, 31, 16))
    carryover = zeros(16)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                for l in range(nlu):
                    pervaccum[l] = carryover[l]
                    pervaccum[l] = (pervaccum[l] * exp(-0.12) + (1 / 0.12) * (1 - exp(-0.12)))
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            washperv[Y][i][j][l] = (1 - math.exp(-1.81 * qrunp[Y][i][j][l])) * pervaccum[l]
                            pervaccum[l] -= washperv[Y][i][j][l]
                else:
                    pass
                for l in range(nlu):
                    carryover[l] = pervaccum[l]
    return washperv


def WashPerv_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNP_0, AntMoist_0, Grow_0, NRur, NUrb):
    nlu = NLU(NRur, NUrb)
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    qrunp = QrunP_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow_0)
    return WashPerv_inner(NYrs, DaysMonth, Temp, NRur, nlu, water, qrunp)
