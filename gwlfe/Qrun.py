import numpy as np
from Timer import time_function
from Water import Water, Water_2
from Retention import Retention, Retention_2
from NLU import NLU
from Memoization import memoize


@memoize
def Qrun(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    retention = Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        result[Y][i][j][l] = 0
                        if CN[l] > 0:
                            if water[Y][i][j] >= 0.2 * retention[Y][i][j][l]:
                                result[Y][i][j][l] = (water[Y][i][j] - 0.2 * retention[Y][i][j][l]) ** 2 / (
                                        water[Y][i][j] + 0.8 * retention[Y][i][j][l])
    return result


@memoize
def Qrun_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu))
    water = np.repeat(Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], nlu, axis=3)
    TempE = np.repeat(Temp[:, :, :, None], nlu, axis=3)
    cnrur = np.tile(CN[None, None, None, :], (NYrs, 12, 31, 1))
    retention = Retention_2(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0)
    retention02 = 0.2 * retention
    # val = np.zeros((NYrs, 12, 31, nlu))
    nonzero = np.where((TempE > 0) & (water > 0.01) & (water >= retention02) & (cnrur > 0))
    result[nonzero] = (water[nonzero] - retention02[nonzero]) ** 2 / (water[nonzero] + 0.8 * retention[nonzero])
    return result
