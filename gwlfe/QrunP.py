import numpy as np
from Timer import time_function
from NLU import NLU
from Water import Water, Water_2
from CNP import CNP, CNP_2
from CNumPervReten import CNumPervReten, CNumPervReten_2
from numba import jit
# @time_function
def QrunP(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow):
    result = np.zeros((NYrs, 12, 31, 16))  # TODO: should this be nlu?
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    cnp = CNP(NRur, NUrb, CNP_0)
    c_num_perv_reten = CNumPervReten(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNP_0, Grow)
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

# @time_function

def QrunP_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu))
    water = np.repeat(Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], nlu, axis=3)
    TempE = np.repeat(Temp[:, :, :, None], nlu, axis=3)
    c_num_perv_reten = CNumPervReten_2(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNP_0, Grow)
    c_num_perv_reten02 = 0.2 * c_num_perv_reten
    cnp = CNP_2(NRur, NUrb, CNP_0)
    cnp_1 = np.tile(cnp[1][None, None, None, :], (NYrs, 12, 31, 1))
    val = (water - c_num_perv_reten02)**2/(water + 0.8 * c_num_perv_reten)
    result[np.where((TempE>0) &(water>=0.05) & (cnp_1>0) & ( water >= c_num_perv_reten02))] = val[np.where((TempE>0) &(water>=0.05) & (cnp_1>0) & ( water >= c_num_perv_reten02))]
    return result