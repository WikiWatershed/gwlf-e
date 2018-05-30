import numpy as np
from Timer import time_function
from NLU import NLU
from Water import Water, Water_2
from CNI import CNI, CNI_2
from CNumImpervReten import CNumImpervReten, CNumImpervReten_2
from Memoization import memoize


@memoize
def QrunI(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow_0):
    result = np.zeros((NYrs, 12, 31, 16))  # TODO: should this be nlu?
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    cni = CNI(NRur, NUrb, CNI_0)
    c_num_imperv_reten = CNumImpervReten(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNI_0, Grow_0)
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
                            if cni[1][l] > 0:
                                if water[Y][i][j] >= 0.2 * c_num_imperv_reten[Y][i][j][l]:
                                    result[Y][i][j][l] = (water[Y][i][j] - 0.2 * c_num_imperv_reten[Y][i][j][
                                        l]) ** 2 / (
                                                                 water[Y][i][j] + 0.8 * c_num_imperv_reten[Y][i][j][l])
    return result


# @time_function
@memoize
def QrunI_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow_0):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu))
    water = np.repeat(Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], nlu, axis=3)
    TempE = np.repeat(Temp[:, :, :, None], nlu, axis=3)
    cni = CNI_2(NRur, NUrb, CNI_0)
    cni_1 = np.tile(cni[1][None, None, None, :], (NYrs, 12, 31, 1))
    c_num_imperv_reten = CNumImpervReten_2(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNI_0,
                                           Grow_0)
    c_num_imperv_reten02 = 0.2 * c_num_imperv_reten
    nonzero = np.where((TempE > 0) & (water >= 0.05) & (cni_1 > 0) & (water >= c_num_imperv_reten02))
    result[nonzero] = (water[nonzero] - c_num_imperv_reten02[nonzero]) ** 2 / (
                water[nonzero] + 0.8 * c_num_imperv_reten[nonzero])
    return result
