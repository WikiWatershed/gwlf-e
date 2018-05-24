import numpy as np
from Timer import time_function
import math
from Memoization import memoize
from NLU import NLU
from Water import Water
from QrunP import QrunP


@memoize
def WashPerv(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNP_0, AntMoist_0, Grow, NRur, NUrb):
    pervaccum = np.zeros(16)
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    qrunp = QrunP(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow)
    washperv = np.zeros((NYrs, 12, 31, 16))
    carryover = np.zeros(16)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                for l in range(nlu):
                    pervaccum[l] = carryover[l]
                    pervaccum[l] = (pervaccum[l] * np.exp(-0.12) + (1 / 0.12) * (1 - np.exp(-0.12)))
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.05:
                    for l in range(NRur, nlu):
                        washperv[Y][i][j][l] = (1 - math.exp(-1.81 * qrunp[Y][i][j][l])) * pervaccum[l]
                        pervaccum[l] -= washperv[Y][i][j][l]
                else:
                    pass
                for l in range(nlu):
                    carryover[l] = pervaccum[l]
    return washperv


def PervAccum_2():
    pass
