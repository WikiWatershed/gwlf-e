import numpy as np
from Timer import time_function
import math
from Memoization import memoize
from NLU import NLU
from Water import Water
from QrunI import QrunI


@memoize
def WashImperv(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, AntMoist_0, Grow, NRur, NUrb):
    result = np.zeros((NYrs, 12, 31, 16))
    impervaccum = np.zeros(16)
    carryover = np.zeros(16)
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    qruni = QrunI(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                for l in range(nlu):
                    impervaccum[l] = carryover[l]
                    impervaccum[l] = (impervaccum[l] * np.exp(-0.12) + (1 / 0.12) * (1 - np.exp(-0.12)))
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            result[Y][i][j][l] = (1 - math.exp(-1.81 * qruni[Y][i][j][l])) * impervaccum[l]
                            impervaccum[l] -= result[Y][i][j][l]
                else:
                    pass
                for l in range(nlu):
                    carryover[l] = impervaccum[l]
    return result



def WashImperv_2():
    pass
