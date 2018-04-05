import numpy as np
from Timer import time_function
from CNP import CNP
from CNumPerv import CNumPerv
from NLU import NLU
from Water import Water


def CNumPervReten(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNP_0, Grow):
    cnp = CNP(NRur, NUrb, CNP_0)
    c_num_perv = CNumPerv(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow, AntMoist_0)
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
                            if cnp[1][l] > 0:
                                result[Y][i][j][l] = 2540 / c_num_perv[Y][i][j][l] - 25.4
                                if result[Y][i][j][l] < 0:
                                    result[Y][i][j][l] = 0
    return result


def CNumPervReten_2():
    pass
