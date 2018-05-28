import numpy as np
from Timer import time_function
from CNI import CNI, CNI_2
from CNumImperv import CNumImperv, CNumImperv_2
from NLU import NLU
from Water import Water, Water_2
from Memoization import memoize

# @time_function
@memoize
def CNumImpervReten(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNI_0,
                    Grow_0):  # TODO: this is exactly the same as perv and retention
    cni = CNI(NRur, NUrb, CNI_0)
    c_num_imperv = CNumImperv(NYrs, NRur, NUrb, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, Grow_0, AntMoist_0)
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

# @time_function
@memoize
def CNumImpervReten_2(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CNI_0, Grow_0):
    cni = CNI_2(NRur, NUrb, CNI_0)
    cni_1 = np.tile(cni[1][None, None, None, :], (NYrs, 12, 31, 1))
    c_num_imperv = CNumImperv_2(NYrs, NRur, NUrb, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, Grow_0, AntMoist_0)
    nlu = NLU(NRur, NUrb)
    water = np.repeat(Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], nlu, axis=3)
    result = np.zeros((NYrs, 12, 31, nlu))
    TempE = np.repeat(Temp[:, :, :, None], nlu, axis=3)
    result[np.where((TempE>0) & (water >= 0.05) & (cni_1>0))] =  2540 / c_num_imperv[np.where((TempE>0) & (water >= 0.05) & (cni_1>0))] - 25.4
    result[np.where(result<0)] = 0
    return result