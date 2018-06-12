from numpy import repeat
from numpy import tile
from numpy import where
from numpy import zeros

from CNP import CNP, CNP_2
from CNumPervReten import CNumPervReten, CNumPervReten_2
from Memoization import memoize
# from Timer import time_function
from NLU import NLU
from Water import Water, Water_2


@memoize
def QrunP(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow_0):
    result = zeros((NYrs, 12, 31, 16))  # TODO: should this be nlu?
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    cnp = CNP(NRur, NUrb, CNP_0)
    c_num_perv_reten = CNumPervReten(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNP_0, Grow_0)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur, nlu):  # TODO: what is this for?
                        result[Y][i][j][l] = 0
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            if cnp[1][l] > 0:
                                if water[Y][i][j] >= 0.2 * c_num_perv_reten[Y][i][j][l]:
                                    result[Y][i][j][l] = (water[Y][i][j] - 0.2 * c_num_perv_reten[Y][i][j][l]) ** 2 / (
                                            water[Y][i][j] + 0.8 * c_num_perv_reten[Y][i][j][l])
    return result


@memoize
def QrunP_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu))
    water = repeat(Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], nlu, axis=3)
    TempE = repeat(Temp[:, :, :, None], nlu, axis=3)
    c_num_perv_reten = CNumPervReten_2(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNP_0, Grow_0)
    c_num_perv_reten02 = 0.2 * c_num_perv_reten
    cnp = CNP_2(NRur, NUrb, CNP_0)
    cnp_1 = tile(cnp[1][None, None, None, :], (NYrs, 12, 31, 1))
    nonzero = where((TempE > 0) & (water >= 0.05) & (cnp_1 > 0) & (water >= c_num_perv_reten02))
    result[nonzero] = (water[nonzero] - c_num_perv_reten02[nonzero]) ** 2 / (
            water[nonzero] + 0.8 * c_num_perv_reten[nonzero])
    return result
