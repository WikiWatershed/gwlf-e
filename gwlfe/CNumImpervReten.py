import numpy as np
from Timer import time_function
from CNI import CNI
from CNumImperv import CNumImperv
from NLU import NLU
from Water import Water
from Memoization import memoize


@memoize
def CNumImpervReten(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNI_0,
                    Grow):  # TODO: this is exactly the same as perv and retention
    cni = CNI(NRur, NUrb, CNI_0)
    c_num_imperv = CNumImperv(NYrs, NRur, NUrb, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, Grow, AntMoist_0)
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    result = np.zeros((NYrs, 12, 31, nlu))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:  # missing
                    if water[Y][i][j] < 0.05:  # missing
                        pass
                    else:
                        for l in range(NRur, nlu):
                            if cni[1][l] > 0:
                                result[Y][i][j][l] = 2540 / c_num_imperv[Y][i][j][l] - 25.4
                                if result[Y][i][j][l] < 0:
                                    result[Y][i][j][l] = 0
    return result


def CNumImpervReten_2():
    pass
