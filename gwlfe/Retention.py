import numpy as np
from Timer import time_function
from NLU import NLU
from CNum import CNum, CNum_1
from Water import Water, Water_2
# @time_function
def Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu)) # Why nlu ?
    c_num = CNum(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        if CN[l] > 0:#TODO:CN is set to zero in datamodel
                            result[Y][i][j][l] = 2540 / c_num[Y][i][j][l] - 25.4
                            if result[Y][i][j][l] < 0:
                                result[Y][i][j][l] = 0
    return result

# @time_function
def Retention_2(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu))
    c_num = CNum_1(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow)
    cnrur = np.tile(CN[:NRur][None, None, None, :], (NYrs, 12, 31, 1))
    water = np.repeat(Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:,:,:,None],NRur, axis=3 )
    TempE = np.repeat(Temp[:, :, :, None], NRur, axis=3)
    result[np.where((TempE>0) & (water > 0.01) & (cnrur > 0))] = 2540 / c_num[np.where((TempE>0) & (water > 0.01) & (cnrur>0))] - 25.4
    result[np.where(result<0)] = 0
    return result
